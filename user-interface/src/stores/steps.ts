import { ref, computed, type Component } from 'vue'
import { defineStore } from 'pinia'

import CollectKnowledge from '@/components/CollectKnowledge.vue'
import LoadingModel from '@/components/LoadingModel.vue'
import EvaluateQuestion from '@/components/EvaluateQuestion.vue'

const steps: Component = [
  CollectKnowledge,
  LoadingModel,
  EvaluateQuestion
]

export const useStepsStore = defineStore('steps', () => {
  const indexStep = ref(0)

  const getCurrentComponent = computed(() => steps[indexStep.value])

  function nextStep() {
    indexStep.value++
  }

  return { steps, getCurrentComponent, nextStep }
})
