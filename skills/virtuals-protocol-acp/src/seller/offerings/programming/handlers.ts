import type { ExecuteJobResult, ValidationResult } from "../../runtime/offeringTypes.js";

// Halal Programming Service
// Only accepts legitimate, non-harmful projects

// Projects that we WILL NOT accept (haram)
const HARAM_PROJECTS = [
  'porn', 'sex', 'gambling', 'casino', 'alcohol', 'drugs',
  'weapon', 'military', 'hacking', 'malware', 'spyware',
  'fraud', 'scam', 'phishing', 'hate', 'terrorism'
];

function isProjectHalal(description: string): boolean {
  const lowerDesc = description.toLowerCase();
  for (const keyword of HARAM_PROJECTS) {
    if (lowerDesc.includes(keyword)) {
      return false;
    }
  }
  return true;
}

export async function executeJob(request: any): Promise<ExecuteJobResult> {
  const { task, language, description } = request;
  
  if (!task || !description) {
    return { 
      deliverable: JSON.stringify({ 
        error: "Missing required fields: task, description" 
      }) 
    };
  }
  
  if (!isProjectHalal(description)) {
    return { 
      deliverable: JSON.stringify({ 
        error: "Cannot accept: We only provide halal programming services." 
      }) 
    };
  }
  
  // Placeholder - in production, integrate with code execution API
  return { 
    deliverable: JSON.stringify({ 
      task,
      language,
      description,
      result: "[Programming service - to be implemented]",
      note: "Halal programming: ethical AI, educational tools, productivity apps, etc."
    }) 
  };
}

export function validateRequirements(request: any): ValidationResult {
  const { task, description } = request;
  
  if (!task || !description) {
    return { 
      valid: false, 
      reason: "Missing required fields: task, description" 
    };
  }
  
  if (!isProjectHalal(description)) {
    return { 
      valid: false, 
      reason: "We only provide halal programming services." 
    };
  }
  
  return { valid: true };
}

export function requestPayment(request: any): string {
  return "Halal programming service - ethical projects only";
}
