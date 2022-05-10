# -*- mode: python; python-indent: 4 -*-
import ncs
from ncs.application import Service


class ServiceCallbacks(Service):
    @Service.create
    def cb_create(self, tctx, root, service, proplist):
        self.log.info(f'External-Plan create: {service._path}')

        vars = ncs.template.Variables()
        vars.add('SERVICE_LOCATION', service.service_path)
        if service.plan_path:
            vars.add('PLAN_LOCATION', service.plan_path)
        else:
            vars.add('PLAN_LOCATION', '/external-plan:external-plan/external-plan')

        template = ncs.template.Template(service)
        template.apply('external-plan-template', vars)
