import { ref, computed, type Component } from 'vue'
import { defineStore } from 'pinia'

import CollectKnowledge from '@/components/CollectKnowledge.vue'
import EvaluateQuestion from '@/components/EvaluateQuestion.vue'
import GenerateQuestion from '@/components/GenerateQuestion.vue'

import { ProcessStep } from '@/services/knowledgeWorklow'

const steps: Component = [
  CollectKnowledge,
  GenerateQuestion,
  EvaluateQuestion
]

export const useStepStore = defineStore('step', () => {
  const indexStep = ref(0)

  const getCurrentComponent = computed(() => steps[indexStep.value])

  function nextStep() {
    if(indexStep.value + 1 < steps.length)
      indexStep.value++
    else
      indexStep.value = 0
  }

  function goToStep(processStep: ProcessStep){
    indexStep.value = processStep
  }

  return { indexStep, steps, getCurrentComponent, nextStep, goToStep }
})
