import type { Job, ServiceContext } from '../../types';

export async function executeJob(job: Job, context: ServiceContext) {
  const { userPrompt } = job;
  
  // Analyze the project for ethical concerns
  const concerns: string[] = [];
  const suggestions: string[] = [];
  
  // Check for harmful content
  const harmfulKeywords = ['hack', 'steal', 'spam', 'fake', 'scam', 'harm', 'attack', 'exploit', 'virus', 'malware', 'phish', 'fraud'];
  const lowerPrompt = userPrompt.toLowerCase();
  
  for (const keyword of harmfulKeywords) {
    if (lowerPrompt.includes(keyword)) {
      concerns.push(`Potential concern: "${keyword}" - please clarify the legitimate purpose.`);
    }
  }
  
  // Add core ethical principles
  suggestions.push("Core principle: Always ask 'Is this just?' before proceeding.");
  suggestions.push("Consider: Does this harm anyone?");
  suggestions.push("Consider: Is this truthful?");
  suggestions.push("Consider: Would you be comfortable if this affected you?");
  
  const response = concerns.length > 0
    ? `⚠️ Please clarify:\n${concerns.join('\n')}\n\nOnce you clarify, I can provide more specific guidance.`
    : `✅ Your project appears to align with ethical principles.\n\nSuggestions:\n${suggestions.join('\n')}`;
  
  return {
    success: true,
    result: response
  };
}
