##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# xUPS Device object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################


from Globals import InitializeClass

from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenModel.ZenossSecurity import ZEN_VIEW

from copy import deepcopy

class xupsDevice(Device):
    meta_type = portal_type = 'xupsDevice'


    _relations = Device._relations + (
        ('xupsBattery',       ToManyCont(ToOne, 'ZenPacks.community.xUPS.xupsBattery',       'xupsDevBattery',),),
        ('xupsInput',         ToManyCont(ToOne, 'ZenPacks.community.xUPS.xupsInput',         'xupsDevInput',),),
        ('xupsOutput',        ToManyCont(ToOne, 'ZenPacks.community.xUPS.xupsOutput',        'xupsDevOutput',),),
        ('xupsBypass',        ToManyCont(ToOne, 'ZenPacks.community.xUPS.xupsBypass',        'xupsDevBypass',),),
        ('xupsContactSense',  ToManyCont(ToOne, 'ZenPacks.community.xUPS.xupsContactSense',  'xupsDevContactSense',),),
    )

InitializeClass(xupsDevice)
