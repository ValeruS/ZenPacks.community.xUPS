##########################################################################
# Author:               ValeruS
# Date:                 Septeber 2017
# Revised:
#
# xupsOutput object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__="""xupsOutput

xupsOutput is a component of a xUPS Device

"""

from Globals import InitializeClass

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class xupsOutput(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "xupsOutput"

    xupsOutputPhaseText          = ''
    xupsOutputVoltage            = 0
    xupsOutputCurrent            = 0
    xupsOutputWatts              = 0
    upsOutputPercentLoad         = 0

    _properties = ManagedEntity._properties + (
        {'id': 'xupsOutputPhaseText',         'type': 'string', 'mode': ''},
        {'id': 'xupsOutputVoltage',           'type': 'int',    'mode': ''},
        {'id': 'xupsOutputCurrent',           'type': 'int',    'mode': ''},
        {'id': 'xupsOutputWatts',             'type': 'int',    'mode': ''},
        {'id': 'upsOutputPercentLoad',        'type': 'int',    'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('xupsDevOutput', ToOne(ToManyCont, 'ZenPacks.community.xUPS.xupsDevice', 'xupsOutput', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'xupsOutput',
        'meta_type'      : 'xupsOutput',
        'description'    : """xupsOutput info""",
        'product'        : 'xUPS',
        'immediate_view' : 'viewxupsOutput',
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
        return self.xupsDevOutput()

InitializeClass(xupsOutput)
