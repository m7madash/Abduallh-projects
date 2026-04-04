import type { Job, ServiceContext } from '../../types';

export async function executeJob(job: Job, context: ServiceContext) {
  const { userPrompt } = job;
  
  const response = `Thank you for your data analysis request.\n\nTo help you, please share:\n1. The data you want analyzed\n2. What insights you need\n3. The format you prefer\n\nI will analyze and provide clear, useful insights.`;
  
  return {
    success: true,
    result: response
  };
}
