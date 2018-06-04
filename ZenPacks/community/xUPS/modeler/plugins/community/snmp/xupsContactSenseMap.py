##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# xupsContactSenseMap modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """xupsContactSenseMap

Gather table information from ContactSenseMap based on XUPS-MIB (.1.3.6.1.4.1.534).
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class xupsContactSenseMap(SnmpPlugin):

    maptype = "xupsContactSenseMap"
    modname = "ZenPacks.community.xUPS.xupsContactSense"
    relname = "xupsContactSense"


    snmpGetTableMaps = (
        GetTableMap('xupsContactSenseEntry',
                    '.1.3.6.1.4.1.534.1.6.8.1',
                    {
                       '.2': 'xupsContactType',
                       '.3': 'xupsContactState',
                       '.4': 'xupsContactDescr',
                    }
        ),
    )

    ContactType       = {1:'normallyOpen',
                         2:'normallyClosed',
                         3:'anyChange',
                         4:'notUsed',
                        }

    ContactState      = {1:'open',
                         2:'closed',
                         3:'openWithNotice',
                         4:'closedWithNotice',
                        }

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
#        log.info( "Data= %s", tabledata )
        rm = self.relMap()

        xupsentry = tabledata.get('xupsContactSenseEntry')

# If no data supplied then simply return
        if not xupsentry:
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return

        for oid, data in xupsentry.iteritems():
            try:
                om = self.objectMap(data)
                om.snmpindex = oid.strip('.')
                om.xupsContactTypeText = self.ContactType.get(int(om.xupsContactType), 'unknown')
                om.xupsContactStateText = self.ContactState.get(int(om.xupsContactType), 'unknown')
                om.id = self.prepId(om.xupsContactDescr)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in xupsContactSenseMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
