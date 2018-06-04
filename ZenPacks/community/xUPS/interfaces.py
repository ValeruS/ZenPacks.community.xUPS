##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# interfaces.py for xUPS ZenPack
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""interfaces

describes the form field to the user interface.

"""
from Products.Zuul.form import schema
from Products.Zuul.interfaces.device import IDeviceInfo
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.utils import ZuulMessageFactory as _t

from Products.ZenModel.ZVersion import VERSION as ZENOSS_VERSION
from Products.ZenUtils.Version import Version

if Version.parse('Zenoss %s' % ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine


class IxupsBatteryInfo(IComponentInfo):
    xupsBatVoltage              = SingleLineText(title=_t(u"Voltage"))
    xupsBatCurrent              = SingleLineText(title=_t(u"Current"))
    xupsBatCapacity             = SingleLineText(title=_t(u"Capacity %"))
    xupsBatTimeRemaining        = SingleLineText(title=_t(u"TimeRemaining(min)"))
    xupsBatteryAbmStatus        = SingleLineText(title=_t(u"Battery Management"))
    upsBatteryStatus            = SingleLineText(title=_t(u"Battery Status"))
    xupsTestBatteryStatus       = SingleLineText(title=_t(u"Battery Test Status"))
    xupsBatteryLastReplacedDate = SingleLineText(title=_t(u"Last Replaced"))

class IxupsInputInfo(IComponentInfo):
    xupsInputVoltage            = SingleLineText(title=_t(u"Input Voltage"))
    xupsInputCurrent            = SingleLineText(title=_t(u"Input Current"))

class IxupsOutputInfo(IComponentInfo):
    xupsOutputVoltage           = SingleLineText(title=_t(u"Output Voltage"))
    xupsOutputCurrent           = SingleLineText(title=_t(u"Output Current"))
    xupsOutputWatts             = SingleLineText(title=_t(u"Output Watts"))
    upsOutputPercentLoad        = SingleLineText(title=_t(u"Percent Load"))

class IxupsBypassInfo(IComponentInfo):
    xupsBypassVoltage           = SingleLineText(title=_t(u"Bypass Voltage"))

class IxupsContactSenseInfo(IComponentInfo):
    xupsContactDescr            = SingleLineText(title=_t(u"Name"))
    xupsContactType             = SingleLineText(title=_t(u"Type"))
    xupsContactState            = SingleLineText(title=_t(u"State"))
