import axios from 'axios'

let $axios = axios.create({
  baseURL: '/api/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

$axios.post('/api/')
// Request Interceptor
$axios.interceptors.request.use(function (config) {
  config.headers['Authorization'] = 'Fake Token'
  return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // Handle Error
  console.log(error)
  return Promise.reject(error)
})

export default {

  fetchResource () {
    return $axios.get(`resource/xxx`)
      .then(response => response.data)
  },

  fetchSecureResource () {
    return $axios.get(`secure-resource/zzz`)
      .then(response => response.data)
  },
  get () {

  },
  Search (keywords, paras) {
    console.log(keywords, paras)
    return $axios.post('search', { // params参数必写 , 如果没有参数传{}也可以
      data: {
        key: keywords,
        para: paras
      }
    })
      .then(response => response.data)
  },

  fetchDemo10 () {
    return $axios.get(`demo10`)
      .then(response => response.data)
  }
}
