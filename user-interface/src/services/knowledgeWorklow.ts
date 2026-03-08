import type { Knowledge, Metric, Question } from "@/types/types"
import api from "@/services/api"
import type { AxiosResponse } from "axios"

const processFlow = ["CollectKnowledge", "GenerateQuestion", "EvaluateQuestion", "Done"]

//From user action in worlfow
export enum ProcessStep {
    CollectKnowledge,
    WaitGeneration,
    EvaluateQuestion,
    ProcessDone
}

export async function identifyProcessStep(knowledge: Knowledge | null): Promise<ProcessStep>{
        if (knowledge == null)
            return ProcessStep.CollectKnowledge

        //Check questions exist
        const apiGetQuestions: AxiosResponse<Question[]> = await api.get(
            `api/v1/knowledges/${knowledge.id}/questions/`, 
            {
                validateStatus: function (status) {
                    return status < 500
                },
            })
        if (apiGetQuestions.status >= 400 && apiGetQuestions.status < 500)
            return ProcessStep.WaitGeneration

        const questions: Question[] = apiGetQuestions.data
        if (questions.length == 0)
            return ProcessStep.WaitGeneration
        
        //Check metrics exist
        const apiGetMetrics: AxiosResponse<Metric[]> = await api.get(
            `api/v1/questions/${questions[0]!.id}/metrics/`, 
            {
                validateStatus: function (status) {
                    return status < 500
                },
            })
        if (apiGetMetrics.status >= 400 && apiGetMetrics.status < 500)
            return ProcessStep.EvaluateQuestion
        
        const metrics: Metric[] = apiGetMetrics.data
        if (metrics.length == 0)
            return ProcessStep.EvaluateQuestion

        //Data is complete
        return ProcessStep.ProcessDone
    }
    
    
    