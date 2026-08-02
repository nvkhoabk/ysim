import type { NextRequest } from 'next/server';

import { operatorLogoutResponse } from '../../../lib/operator-logout';

export const dynamic = 'force-dynamic';

export function POST(request: NextRequest) {
  return operatorLogoutResponse(request);
}
