##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# info.py for xUPS ZenPack
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""info.py

Representation of xUPS components.

"""


from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info

from ZenPacks.community.xUPS import interfaces



class xupsBatteryInfo(ComponentInfo):
    implements(interfaces.IxupsBatteryInfo)

    xupsBatTimeRemaining        = ProxyProperty("xupsBatTimeRemaining")
    xupsBatVoltage              = ProxyProperty("xupsBatVoltage")
    xupsBatCurrent              = ProxyProperty("xupsBatCurrent")
    xupsBatCapacity             = ProxyProperty("xupsBatCapacity")
    xupsBatteryAbmStatus        = ProxyProperty("xupsBatteryAbmStatus")
    xupsBatteryAbmStatusText    = ProxyProperty("xupsBatteryAbmStatusText")
    xupsBatteryLastReplacedDate = ProxyProperty("xupsBatteryLastReplacedDate")
    xupsTestBatteryStatus       = ProxyProperty("xupsTestBatteryStatus")
    xupsTestBatteryStatusText   = ProxyProperty("xupsTestBatteryStatusText")
    upsBatteryStatus            = ProxyProperty("upsBatteryStatus")
    upsBatteryStatusText        = ProxyProperty("upsBatteryStatusText")

class xupsInputInfo(ComponentInfo):
    implements(interfaces.IxupsInputInfo)

    xupsInputPhaseText          = ProxyProperty("xupsInputPhaseText")
    xupsInputVoltage            = ProxyProperty("xupsInputVoltage")
    xupsInputCurrent            = ProxyProperty("xupsInputCurrent")

class xupsOutputInfo(ComponentInfo):
    implements(interfaces.IxupsOutputInfo)

    xupsOutputPhaseText         = ProxyProperty("xupsOutputPhaseText")
    xupsOutputVoltage           = ProxyProperty("xupsOutputVoltage")
    xupsOutputCurrent           = ProxyProperty("xupsOutputCurrent")
    xupsOutputWatts             = ProxyProperty("xupsOutputWatts")
    upsOutputPercentLoad        = ProxyProperty("upsOutputPercentLoad")

class xupsBypassInfo(ComponentInfo):
    implements(interfaces.IxupsBypassInfo)

    xupsBypassPhaseText         = ProxyProperty("xupsBypassPhaseText")
    xupsBypassVoltage           = ProxyProperty("xupsBypassVoltage")

class xupsContactSenseInfo(ComponentInfo):
    implements(interfaces.IxupsContactSenseInfo)

    xupsContactType             = ProxyProperty("xupsContactType")
    xupsContactTypeText         = ProxyProperty("xupsContactTypeText")
    xupsContactState            = ProxyProperty("xupsContactState")
    xupsContactStateText        = ProxyProperty("xupsContactStateText")
    xupsContactDescr            = ProxyProperty("xupsContactDescr")
