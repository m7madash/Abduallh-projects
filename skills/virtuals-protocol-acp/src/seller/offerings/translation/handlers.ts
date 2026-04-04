import type { ExecuteJobResult, ValidationResult } from "../../runtime/offeringTypes.js";

// Halal Translation Service
// Only accepts legitimate, non-harmful content

// Content that we WILL NOT translate (haram)
const HARAM_KEYWORDS = [
  'porn', 'sex', 'gambling', 'alcohol', 'drugs', 'fraud',
  'violence', 'hate', 'terrorism', 'scam'
];

function isContentHalal(text: string): boolean {
  const lowerText = text.toLowerCase();
  for (const keyword of HARAM_KEYWORDS) {
    if (lowerText.includes(keyword)) {
      return false;
    }
  }
  return true;
}

export async function executeJob(request: any): Promise<ExecuteJobResult> {
  const { text, sourceLanguage, targetLanguage } = request;
  
  // Validate input
  if (!text || !sourceLanguage || !targetLanguage) {
    return { 
      deliverable: JSON.stringify({ 
        error: "Missing required fields: text, sourceLanguage, targetLanguage" 
      }) 
    };
  }
  
  // Check if content is halal
  if (!isContentHalal(text)) {
    return { 
      deliverable: JSON.stringify({ 
        error: "Cannot translate: Content not allowed. We only provide halal translation services." 
      }) 
    };
  }
  
  // TODO: Integrate with translation API
  // For now, return a placeholder
  // In production, use Google Translate, DeepL, or similar API
  
  return { 
    deliverable: JSON.stringify({ 
      originalText: text,
      sourceLanguage,
      targetLanguage,
      translatedText: "[Translation service - to be implemented]",
      note: "This is a placeholder. Integration with translation API needed."
    }) 
  };
}

export function validateRequirements(request: any): ValidationResult {
  const { text, sourceLanguage, targetLanguage } = request;
  
  // Check required fields
  if (!text || !sourceLanguage || !targetLanguage) {
    return { 
      valid: false, 
      reason: "Missing required fields: text, sourceLanguage, targetLanguage" 
    };
  }
  
  // Check content is halal
  if (!isContentHalal(text)) {
    return { 
      valid: false, 
      reason: "We only provide halal translation services. Content not allowed." 
    };
  }
  
  return { valid: true };
}

export function requestPayment(request: any): string {
  return "Halal translation service - work will begin after confirmation";
}
