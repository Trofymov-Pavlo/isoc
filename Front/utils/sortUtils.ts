/**
 * Extract the first alphabetic character from a string,
 * ignoring leading non-alphabetic characters
 */
export function getAlphabeticSortKey(text: string): string {
  if (!text) return '';
  
  // Remove leading non-alphabetic characters
  const cleanText = text.replace(/^[^a-zA-Z]+/, '');
  return cleanText.toLowerCase();
}

/**
 * Sort comparator that ignores leading non-alphabetic characters
 */
export function compareAlphabetic(a: string, b: string): number {
  const keyA = getAlphabeticSortKey(a);
  const keyB = getAlphabeticSortKey(b);
  
  if (keyA === keyB) return 0;
  return keyA < keyB ? -1 : 1;
}
