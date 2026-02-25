import { ref, computed, type Component } from 'vue'
import { defineStore } from 'pinia'

import CollectKnowledge from '@/components/CollectKnowledge.vue'
import EvaluateQuestion from '@/components/EvaluateQuestion.vue'
import GenerateQuestion from '@/components/GenerateQuestion.vue'

const steps: Component = [
  CollectKnowledge,
  GenerateQuestion,
  EvaluateQuestion
]

export const useStepStore = defineStore('step', () => {
  const indexStep = ref(0)

  const getCurrentComponent = computed(() => steps[indexStep.value])

  function nextStep() {
    indexStep.value++
  }

  return { steps, getCurrentComponent, nextStep }
})
