export default [
  {
    files: ['scripts/vs-r1-004/*.mjs'],
    languageOptions: {
      ecmaVersion: 2024,
      sourceType: 'module',
      globals: {
        AbortSignal: 'readonly',
        Buffer: 'readonly',
        clearTimeout: 'readonly',
        console: 'readonly',
        fetch: 'readonly',
        process: 'readonly',
        setTimeout: 'readonly',
        structuredClone: 'readonly',
      },
    },
    rules: {
      eqeqeq: 'error',
      'no-eval': 'error',
      'no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
      'prefer-const': 'error',
    },
  },
];
