odoo.define("fieldservice_worker_geolocalize.person_geolocation", function (require) {
    "use strict";

    var FormController = require("web.FormController");

    FormController.include({
        _onButtonClicked: function (event) {
            if (event.data.attrs.id === "marky") {
                console.log("_onButtonClicked()....");
                console.log(arguments);
                console.log(event);
                this.res_id = event.data.record.res_id;
                this.update_attendance();
            }
            this._super(event);
        },

        update_attendance: function () {
            var self = this;
            var options = {
                enableHighAccuracy: true,
                timeout: 5000,
                maximumAge: 0,
            };
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    self._manual_attendance.bind(self),
                    self._getPositionError,
                    options
                );
            }
        },

        _manual_attendance: function (position) {
            console.log("_manual_attendance...");
            console.log(this);
            this._rpc({
                model: "fsm.person",
                method: "geo_update_location",
                args: [
                    self.res_id,
                    position.coords.latitude,
                    position.coords.longitude,
                ],
            }).then(function (result) {
                // Do nothing
                console.log("then...");
                console.log(result);
            });
        },
        _getPositionError: function (error) {
            console.warn("ERROR(${error.code}): ${error.message}");
            console.log(error.code);
            console.log(error.message);
        },
    });
});
