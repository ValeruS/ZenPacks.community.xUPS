/*
 * Based on the configuration in ../../configure.zcml this JavaScript will only
 * be loaded when the user is looking at an ExampleDevice in the web interface.
 */

(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.xupsBatteryPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'xupsBattery',
            alias:['widget.xupsBatteryPanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'xupsBatteryAbmStatusText'},
                {name: 'upsBatteryStatus'},
                {name: 'upsBatteryStatusText'},
                {name: 'xupsTestBatteryStatusText'},
                {name: 'xupsBatteryLastReplacedDate'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Object Name'),
                width: 100
            },{
                id: 'upsBatteryStatusText',
                dataIndex: 'upsBatteryStatusText',
                header: _t('Battery Status'),
                sortable: true,
                width: 100,
            },{
                id: 'upsBatteryStatus',
                dataIndex: 'upsBatteryStatus',
                header: _t('Status'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50,
            },{
                id: 'xupsBatteryAbmStatusText',
                dataIndex: 'xupsBatteryAbmStatusText',
                header: _t('Battery Management'),
                sortable: true,
                width: 150,
            },{
                id: 'xupsTestBatteryStatusText',
                dataIndex: 'xupsTestBatteryStatusText',
                header: _t('Battery TestStatus'),
                sortable: true,
                width: 150,
            },{
                id: 'xupsBatteryLastReplacedDate',
                flex: 1,
                dataIndex: 'xupsBatteryLastReplacedDate',
                header: _t('Last Replaced Date'),
                sortable: true,
                width: 100,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.xupsBatteryPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('xupsBatteryPanel', ZC.xupsBatteryPanel);
ZC.registerName('xupsBattery', _t('xUPS Battery'), _t('xUPS Batteries'));

ZC.xupsInputPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'xupsInput',
            alias:['widget.xupsInputPanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'xupsInputVoltage'},
                {name: 'xupsInputCurrent'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                flex: 1,
                dataIndex: 'name',
                header: _t('Name'),
                width: 100
            },{
                id: 'xupsInputVoltage',
                dataIndex: 'xupsInputVoltage',
                header: _t('Input Voltage (Volts)'),
                sortable: true,
                width: 150,
            },{
                id: 'xupsInputCurrent',
                dataIndex: 'xupsInputCurrent',
                header: _t('Input Current (Amps)'),
                sortable: true,
                width: 150,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.xupsInputPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('xupsInputPanel', ZC.xupsInputPanel);
ZC.registerName('xupsInput', _t('xUPS Input'), _t('xUPS Inputs'));

ZC.xupsOutputPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'xupsOutput',
            alias:['widget.xupsOutputPanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'xupsOutputVoltage'},
                {name: 'xupsOutputCurrent'},
                {name: 'xupsOutputWatts'},
                {name: 'upsOutputPercentLoad'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                flex: 1,
                dataIndex: 'name',
                header: _t('Name'),
                width: 100
            },{
                id: 'xupsOutputVoltage',
                dataIndex: 'xupsOutputVoltage',
                header: _t('Output Voltage (Volts)'),
                sortable: true,
                width: 150,
            },{
                id: 'xupsOutputCurrent',
                dataIndex: 'xupsOutputCurrent',
                header: _t('Output Current (Amps)'),
                sortable: true,
                width: 150,
            },{
                id: 'xupsOutputWatts',
                dataIndex: 'xupsOutputWatts',
                header: _t('Output Watts (Watts)'),
                sortable: true,
                width: 150,
            },{
                id: 'upsOutputPercentLoad',
                dataIndex: 'upsOutputPercentLoad',
                header: _t('Percent Load'),
                sortable: true,
                width: 150,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.xupsOutputPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('xupsOutputPanel', ZC.xupsOutputPanel);
ZC.registerName('xupsOutput', _t('xUPS Output'), _t('xUPS Outputs'));

ZC.xupsBypassPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'xupsBypass',
            alias:['widget.xupsBypassPanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'xupsBypassVoltage'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                flex: 1,
                dataIndex: 'name',
                header: _t('Name'),
                width: 100
            },{
                id: 'xupsBypassVoltage',
                dataIndex: 'xupsBypassVoltage',
                header: _t('Bypass Voltage (Volts)'),
                sortable: true,
                width: 150,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.xupsBypassPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('xupsBypassPanel', ZC.xupsBypassPanel);
ZC.registerName('xupsBypass', _t('xUPS Bypass'), _t('xUPS Bypass'));

ZC.xupsContactSensePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'xupsContactSense',
            alias:['widget.xupsContactSensePanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'xupsContactTypeText'},
                {name: 'xupsContactStateText'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                flex: 1,
                dataIndex: 'name',
                header: _t('Name'),
                width: 100
            },{
                id: 'xupsContactTypeText',
                dataIndex: 'xupsContactTypeText',
                header: _t('Type'),
                sortable: true,
                width: 150,
            },{
                id: 'xupsContactStateText',
                dataIndex: 'xupsContactStateText',
                header: _t('State'),
                sortable: true,
                width: 150,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.xupsContactSensePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('xupsContactSensePanel', ZC.xupsContactSensePanel);
ZC.registerName('xupsContactSense', _t('xUPS Contact'), _t('xUPS Contacts'));




})();
