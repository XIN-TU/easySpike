<template>
  <div >
    <a-card :loading="loading" title="Resuts" >
      <a-card-grid style="width:100%;text-align:center">
        <h3> The Results of Spike Sorting</h3>
      </a-card-grid>
    </a-card>
    <a-button style="marginTop: 16px" @click="handleClick">
      Toggle loading
    </a-button>
  </div>
</template>

<script>
const ListData = [
  {
    title: 'Klusta',
    content: 'klusta is an open source package for automatic spike sorting of multielectrode neurophysiological recordings made with probes containing up to a few dozens of sites.'
  },
  {
    title: 'Herdingspikes ',
    content: 'Herdingspikes provides functionality for the detection, localisation and clustering of spike data from dense multielectrode arrays'
  },
  {
    title: 'Tridesclous',
    content: 'The primary goal of tridesclous was to provide a toolkit to teach good practices in spike sorting techniques. Trideslcous is now mature and can be used to sort spike on tetrode up to neuropixel probe recorded dataset'
  }
]
export default {
  props: ['current'],
  data () {
    return {
      loading: true,
      labelCol: { span: 4 },
      wrapperCol: { span: 14 },
      form: {
        name: '',
        region: undefined,
        date1: undefined,
        delivery: false,
        type: [],
        resource: '',
        desc: '' // 后端返回参数 记得后面改
      },
      ListData,
      disable1: true,
      disable2: true,
      disable3: true
    }
  },
  methods: {
    handleClick () {
      this.loading = !this.loading
    },
    onSubmit () {
      console.log('submit!', this.form)
    },
    handleChange (value) {
      console.log(`selected ${value}`)
      switch (value) {
        case 'klusta':
          this.disable1 = false
          this.disable2 = true
          this.disable3 = true
          console.log(this.disable1)
          break
        case 'herdingspikes':
          this.disable1 = true
          this.disable2 = false
          this.disable3 = true
          break
        case 'tridesclous':
          this.disable1 = true
          this.disable2 = true
          this.disable3 = false
          break
      }
      this.current += 1
      this.$emit('changeCurrent', this.current)
    }
  }
}
</script>
