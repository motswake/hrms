frappe.ui.form.on('Employee Scorecard', {
    refresh: function(frm) {
        if (!frm.doc.locked) {
            frm.add_custom_button(__('Refresh KPIs'), function() {
                frappe.call({
                    method: 'hrms.hr.api.scorecard.refresh_scorecard',
                    args: { scorecard: frm.doc.name },
                    callback: function(r) { frm.reload_doc(); }
                });
            });
        }
    }
});
