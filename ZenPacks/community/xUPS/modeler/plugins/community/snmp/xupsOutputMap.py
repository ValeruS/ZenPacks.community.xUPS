##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# xupsOutputMap modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """xupsOutputMap

Gather table information from OutputMap based on XUPS-MIB (.1.3.6.1.4.1.534).
"""

import Globals
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class xupsOutputMap(SnmpPlugin):

    maptype = "xupsOutputMap"
    modname = "ZenPacks.community.xUPS.xupsOutput"
    relname = "xupsOutput"


    snmpGetTableMaps = (
        GetTableMap('xupsOutputEntry',
                    '.1.3.6.1',
                    {
                       '.4.1.534.1.4.4.1.2': 'xupsOutputVoltage',
                       '.4.1.534.1.4.4.1.3': 'xupsOutputCurrent',
                       '.4.1.534.1.4.4.1.4': 'xupsOutputWatts',
                       '.2.1.33.1.4.4.1.5': 'upsOutputPercentLoad',
                    }
        ),
    )

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
#        log.info( "Data= %s", tabledata )
        rm = self.relMap()

        xupsentry = tabledata.get('xupsOutputEntry')

# If no data supplied then simply return
        if not xupsentry:
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return

        for oid, data in xupsentry.iteritems():
            try:
                om = self.objectMap(data)
                om.snmpindex = oid.strip('.')
                om.xupsOutputPhaseText = "OutputPhase" + oid.strip('.')
                om.id = self.prepId(om.xupsOutputPhaseText)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in xupsOutputMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
