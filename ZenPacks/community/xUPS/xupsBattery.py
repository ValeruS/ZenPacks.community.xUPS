##########################################################################
# Author:               ValeruS
# Date:                 Septeber 2017
# Revised:
#
# xupsBattery object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__="""xupsBattery

xupsBattery is a component of a xUPS Device

"""

from Globals import InitializeClass

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class xupsBattery(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "xupsBattery"

    xupsBatTimeRemaining           = 0
    xupsBatVoltage                 = 0
    xupsBatCurrent                 = 0
    xupsBatCapacity                = 0
    xupsBatteryAbmStatus           = 0
    xupsBatteryAbmStatusText       = ''
    xupsBatteryLastReplacedDate    = ''
    xupsTestBatteryStatus          = 0
    xupsTestBatteryStatusText      = ''
    upsBatteryStatus               = 0
    upsBatteryStatusText           = ''

    _properties = ManagedEntity._properties + (
        {'id': 'xupsBatTimeRemaining',          'type': 'int',    'mode': ''},
        {'id': 'xupsBatVoltage',                'type': 'int',    'mode': ''},
        {'id': 'xupsBatCurrent',                'type': 'int',    'mode': ''},
        {'id': 'xupsBatCapacity',               'type': 'int',    'mode': ''},
        {'id': 'xupsBatteryAbmStatus',          'type': 'int',    'mode': ''},
        {'id': 'xupsBatteryAbmStatusText',      'type': 'string', 'mode': ''},
        {'id': 'xupsBatteryLastReplacedDate',   'type': 'string', 'mode': ''},
        {'id': 'xupsTestBatteryStatus',         'type': 'int',    'mode': ''},
        {'id': 'xupsTestBatteryStatusText',     'type': 'string', 'mode': ''},
        {'id': 'upsBatteryStatus',              'type': 'int',    'mode': ''},
        {'id': 'upsBatteryStatusText',          'type': 'string', 'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('xupsDevBattery', ToOne(ToManyCont, 'ZenPacks.community.xUPS.xupsDevice', 'xupsBattery', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'xupsBattery',
        'meta_type'      : 'xupsBattery',
        'description'    : """xupsBattery info""",
        'product'        : 'xUPS',
        'immediate_view' : 'viewxupsBattery',
        'actions'        : 
        (
           {'id'            : 'perfConf',
            'name'          : 'Template',
            'action'        : 'objTemplates',
            'permissions'   : (ZEN_CHANGE_DEVICE,),
           },
        ),
    },)


    # Custom components must always implement the device method. The method
    # should return the device object that contains the component.
    def device(self):
        return self.xupsDevBattery()

InitializeClass(xupsBattery)
