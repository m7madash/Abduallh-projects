import type { ExecuteJobResult, ValidationResult } from "../../runtime/offeringTypes.js";

// Halal Writing Service
// Only accepts legitimate, non-harmful content

const HARAM_TOPICS = [
  'porn', 'sex', 'gambling', 'alcohol', 'drugs',
  'violence', 'hate', 'terrorism', 'fraud', 'scam'
];

function isContentHalal(content: string): boolean {
  const lowerContent = content.toLowerCase();
  for (const keyword of HARAM_TOPICS) {
    if (lowerContent.includes(keyword)) {
      return false;
    }
  }
  return true;
}

export async function executeJob(request: any): Promise<ExecuteJobResult> {
  const { topic, wordCount, style, instructions } = request;
  
  if (!topic || !instructions) {
    return { 
      deliverable: JSON.stringify({ 
        error: "Missing required fields: topic, instructions" 
      }) 
    };
  }
  
  // Check topic and instructions are halal
  const fullContent = `${topic} ${instructions}`;
  if (!isContentHalal(fullContent)) {
    return { 
      deliverable: JSON.stringify({ 
        error: "Cannot accept: We only provide halal writing services." 
      }) 
    };
  }
  
  // Placeholder - in production, integrate with AI writing
  return { 
    deliverable: JSON.stringify({ 
      topic,
      wordCount: wordCount || 500,
      style: style || "informative",
      content: "[Writing service - to be implemented]",
      note: "Halal writing: educational, informative, ethical content only"
    }) 
  };
}

export function validateRequirements(request: any): ValidationResult {
  const { topic, instructions } = request;
  
  if (!topic || !instructions) {
    return { 
      valid: false, 
      reason: "Missing required fields: topic, instructions" 
    };
  }
  
  const fullContent = `${topic} ${instructions}`;
  if (!isContentHalal(fullContent)) {
    return { 
      valid: false, 
      reason: "We only provide halal writing services." 
    };
  }
  
  return { valid: true };
}

export function requestPayment(request: any): string {
  return "Halal writing service - educational and ethical content only";
}
