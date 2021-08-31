# Copyright (C) 2021 TREVI Software
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


import logging

from odoo import api, fields, models

_log = logging.getLogger(__name__)


class FsmPerson(models.Model):
    _inherit = "fsm.person"

    def _compute_latlon(self):
        for rec in self:
            if not rec.shape:
                break
            _log.warning("id: %s", self.id)
            sql = "SELECT \
                   ST_X(ST_Transform(shape, 4326)), \
                   ST_Y(ST_TRANSFORM(shape, 4326)) \
                   FROM fsm_person WHERE id=%s"
            self.env.cr.execute(sql, (tuple(self.id),))
            res = self.env.cr.fetchone()
            _log.warning("res: %s", res)
            _log.warning("shape: %s", rec.shape)
            rec.shape_latitude = res[1]
            rec.shape_longitude = res[0]
            _log.warning(
                "_compute_latlon: %s, %s", rec.shape_latitude, rec.shape_longitude
            )

    # Geometry Field
    shape = fields.GeoPoint("Coordinates")
    shape_latitude = fields.Float(
        string="Latitude",
        compute="_compute_latlon",
        digits=(16, 5),
        store=False,
    )
    shape_longitude = fields.Float(
        string="Longitude",
        compute="_compute_latlon",
        digits=(16, 5),
        store=False,
    )
    stage_name = fields.Char(related="stage_id.name", string="Stage Name")
    # Field for Stage Color
    custom_color = fields.Char(
        related="stage_id.custom_color",
        string="Stage Color",
    )

    def geo_localize(self):
        for rec in self:
            if rec.shape:
                return
            if not rec.shape and rec.partner_id:
                rec.partner_id.geo_localize()
                rec.shape = fields.GeoPoint.from_latlon(
                    self.env.cr,
                    rec.partner_id.partner_latitude,
                    rec.partner_id.partner_longitude,
                )
            _log.warning("geo_localize(): %s", rec.shape)
        return

    @api.model
    def geo_update_location(self, res_id, lat, lon):
        """Update location coordinates of worker."""

        _log.warning("geo_update_location()...")
        if not res_id or not lat or not lon:
            return

        fsmPerson = self.env["fsm.person"]
        worker = fsmPerson.browse(res_id)
        worker.shape = fields.GeoPoint.from_latlon(
            cr=self.env.cr, latitude=lat, longitude=lon
        )
