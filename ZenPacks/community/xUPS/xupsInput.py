##########################################################################
# Author:               ValeruS
# Date:                 Septeber 2017
# Revised:
#
# xupsInput object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__="""xupsInput

xupsInput is a component of a xUPS Device

"""

from Globals import InitializeClass

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class xupsInput(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "xupsInput"

    xupsInputPhaseText           = ''
    xupsInputVoltage             = 0
    xupsInputCurrent             = 0

    _properties = ManagedEntity._properties + (
        {'id': 'xupsInputPhaseText',          'type': 'string', 'mode': ''},
        {'id': 'xupsInputVoltage',            'type': 'int',    'mode': ''},
        {'id': 'xupsInputCurrent',            'type': 'int',    'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('xupsDevInput', ToOne(ToManyCont, 'ZenPacks.community.xUPS.xupsDevice', 'xupsInput', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'xupsInput',
        'meta_type'      : 'xupsInput',
        'description'    : """xupsInput info""",
        'product'        : 'xUPS',
        'immediate_view' : 'viewxupsInput',
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
        return self.xupsDevInput()

InitializeClass(xupsInput)
