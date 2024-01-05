export const tryExceptAwait = async (func, payload) => {
    async function getTry() {
      if (payload) {
        return await func(...payload)
      } else {
        return await func()
      }
    }
  
    try {
      return await getTry()
    } catch (error) {
      if (!error) return {}
      return error
    }
  }