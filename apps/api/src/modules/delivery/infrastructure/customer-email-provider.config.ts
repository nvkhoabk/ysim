export type CustomerEmailMode='disabled'|'dry-run'|'live';
export interface CustomerEmailProviderConfig {mode:CustomerEmailMode;endpoint:string|null;token:string|null;timeoutMs:number;}
export function loadCustomerEmailProviderConfig(env:NodeJS.ProcessEnv=process.env):CustomerEmailProviderConfig{
 const mode=(env.YSIM_CUSTOMER_EMAIL_MODE??'disabled').trim().toLowerCase();
 if(!['disabled','dry-run','live'].includes(mode))throw new Error('YSIM_CUSTOMER_EMAIL_MODE is invalid');
 const timeoutMs=Number(env.YSIM_CUSTOMER_EMAIL_TIMEOUT_MS??'10000');
 if(!Number.isInteger(timeoutMs)||timeoutMs<1000||timeoutMs>30000)throw new Error('YSIM_CUSTOMER_EMAIL_TIMEOUT_MS is invalid');
 const endpoint=env.YSIM_CUSTOMER_EMAIL_ENDPOINT?.trim()||null;
 const token=env.YSIM_CUSTOMER_EMAIL_TOKEN?.trim()||null;
 if(mode==='live'){
  if(!endpoint||!token)throw new Error('Live customer email configuration is incomplete');
  const url=new URL(endpoint);if(url.protocol!=='https:')throw new Error('Live customer email endpoint must use HTTPS');
 }
 return {mode:mode as CustomerEmailMode,endpoint,token,timeoutMs};
}
