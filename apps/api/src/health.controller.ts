import { Controller, Get } from '@nestjs/common';
import type { HealthResponse } from '@ysim/contracts';

const response = (check: HealthResponse['check']): HealthResponse => ({
  check,
  service: 'commissioning-api',
  status: 'ok',
});

@Controller('health')
export class HealthController {
  @Get()
  health(): HealthResponse {
    return response('health');
  }

  @Get('live')
  live(): HealthResponse {
    return response('live');
  }

  @Get('ready')
  ready(): HealthResponse {
    return response('ready');
  }
}
