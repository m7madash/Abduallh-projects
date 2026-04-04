import type { Job, ServiceContext } from '../../types';

export async function executeJob(job: Job, context: ServiceContext) {
  const { userPrompt } = job;
  
  const response = `Research request: "${userPrompt}"\n\nI will research this topic and provide:\n- Key findings\n- Multiple perspectives\n- Reliable sources\n- Balanced analysis\n\nPlease allow time for thorough research.`;
  
  return {
    success: true,
    result: response
  };
}
