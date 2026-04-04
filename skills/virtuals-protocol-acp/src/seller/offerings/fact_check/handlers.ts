import type { Job, ServiceContext } from '../../types';

export async function executeJob(job: Job, context: ServiceContext) {
  const { userPrompt } = job;
  
  // Simple fact check response
  const response = `Thank you for your fact check request: "${userPrompt}"\n\nI will analyze this claim and provide feedback based on ethical principles.\n\nKey questions to consider:\n1. What is the source?\n2. Is there evidence?\n3. Does this harm anyone?\n4. Is this fair and balanced?\n\nNote: For accurate fact checking, please provide the specific claim or statement.`;
  
  return {
    success: true,
    result: response
  };
}
