##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# xupsBypassMap modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """xupsBypassMap

Gather table information from BypassMap based on XUPS-MIB (.1.3.6.1.4.1.534).
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class xupsBypassMap(SnmpPlugin):

    maptype = "xupsBypassMap"
    modname = "ZenPacks.community.xUPS.xupsBypass"
    relname = "xupsBypass"


    snmpGetTableMaps = (
        GetTableMap('xupsBypassEntry',
                    '.1.3.6.1.4.1.534.1.5.3.1',
                    {
                       '.2': 'xupsBypassVoltage',
                    }
        ),
    )

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
#        log.info( "Data= %s", tabledata )
        rm = self.relMap()

        xupsentry = tabledata.get('xupsBypassEntry')

# If no data supplied then simply return
        if not xupsentry:
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return

        for oid, data in xupsentry.iteritems():
            try:
                om = self.objectMap(data)
                om.snmpindex = oid.strip('.')
                om.xupsBypassPhaseText = "BypassPhase" + oid.strip('.')
                om.id = self.prepId(om.xupsBypassPhaseText)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in xupsBypassMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
