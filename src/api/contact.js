import { placeholderApi } from './index'

const basePath = 'contact/'

export default {
  send(payload) {
    // Expecting payload: { name, email, message }
    return placeholderApi.post(basePath, payload)
  }
}
