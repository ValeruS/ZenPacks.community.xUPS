##########################################################################
# Author:               ValeruS
# Date:                 Septeber 2017
# Revised:
#
# xupsContactSense object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__="""xupsContactSense

xupsContactSense is a component of a xUPS Device

"""

from Globals import InitializeClass

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class xupsContactSense(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "xupsContactSense"

    xupsContactType               = 0
    xupsContactTypeText           = ''
    xupsContactState              = 0
    xupsContactStateText          = ''
    xupsContactDescr              = ''

    _properties = ManagedEntity._properties + (
        {'id': 'xupsContactType',              'type': 'int',    'mode': ''},
        {'id': 'xupsContactTypeText',          'type': 'string', 'mode': ''},
        {'id': 'xupsContactState',             'type': 'int',    'mode': ''},
        {'id': 'xupsContactStateTex',          'type': 'string', 'mode': ''},
        {'id': 'xupsContactDescr',             'type': 'string', 'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('xupsDevContactSense', ToOne(ToManyCont, 'ZenPacks.community.xUPS.xupsDevice', 'xupsContactSense', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'xupsContactSense',
        'meta_type'      : 'xupsContactSense',
        'description'    : """xupsContactSense info""",
        'product'        : 'xUPS',
        'immediate_view' : 'viewxupsContactSense',
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
        return self.xupsDevContactSense()

InitializeClass(xupsContactSense)
