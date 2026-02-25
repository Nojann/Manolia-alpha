import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

import type { Knowledge } from '@/types/types'

export const useItemStore = defineStore('item', () => {
    const knowledge = ref<Knowledge>()
  //const indexStep = ref(0)

  //const getCurrentComponent = computed(() => steps[indexStep.value])


  return { knowledge }
})