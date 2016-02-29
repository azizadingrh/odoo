# -*- coding: utf-8 -*-
# Copyright 2016 Numérigraphe
#
import logging
from openerp import tools
_logger = logging.getLogger(__name__)

def migrate(cr, version):
    _logger.info("Removing the view stock_history")
    tools.drop_view_if_exists(cr, 'stock_history')
    _logger.info("Migration done")
