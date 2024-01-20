import axios from "axios"

const debug = true
export const getApiClient = (apiUrl, config) => {
    const apiClient = axios.create({
      baseURL: apiUrl,
      ...config
    })
  
    apiClient.interceptors.response.use(
      function (response) {
        if (debug) {
          console.log('Response:', response)
        }
        return response
      },
      function (error) {
        return Promise.reject(error.response)
      }
    )
  
    apiClient.interceptors.request.use(function (config) {
      if (debug) {
        console.log('Request:', config)
      }
      return config
    })
  
    return apiClient
  }

  export const placeholderApi = getApiClient('http://timtvogt.pythonanywhere.com//api/',{})
