<template>
  <div >
    <a-card :loading="loading" title="Loading Recording" >
    <a-card-grid :style="{width:'30%', textAlign:'center', height:'100%'}">
      <h3>Datasets Selection description</h3>
      <a-list item-layout="horizontal" :data-source="ListData">
        <a-list-item slot="renderItem" slot-scope="item">
          <a-list-item-meta :description= "item.content">
            <a slot="title">{{ item.title }}</a>
          </a-list-item-meta>
        </a-list-item>
      </a-list>
    </a-card-grid>
    <a-card-grid style="width:70%" :hoverable="false">
        <a-form-model :model="form" :label-col="labelCol" :wrapper-col="wrapperCol">
            <!-- <a-form-model-item label="Activity name">
                <a-input v-model="form.name" />
            </a-form-model-item> -->
            <a-form-model-item label="Update by yourself">
                <a-switch v-model="form.delivery" @change="handleChange"/>
            </a-form-model-item>
            <a-form-model-item label="Update dataset">
                <a-upload
                    action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                    :default-file-list="defaultFileList"
                >
                <a-button :disabled = "form.disabled1"> <a-icon type="upload" /> Upload </a-button>
                 </a-upload>
            </a-form-model-item>
            <a-form-model-item label="Datasets type">
                <a-select  placeholder="please select datasets type which you update datastes" :disabled = "form.disabled1">
                    <a-select-option value="mearec">
                        Mearec
                    </a-select-option>
                    <a-select-option value="openephys">
                        Openephys
                    </a-select-option>
                </a-select>
            </a-form-model-item>
            <a-form-model-item label="Select datasets" >
                <a-select placeholder="please select datasets if you do not update datastes" :disabled = 'form.disabled2'>
                    <a-select-option value="testData1">
                        testData1
                    </a-select-option>
                    <a-select-option value="testData2">
                        testData2
                    </a-select-option>
                </a-select>
            </a-form-model-item>
            <a-form-model-item :wrapper-col="{ span: 14, offset: 4 }">
                <a-button type="primary" @click="onSubmit">
                    Confirm
                </a-button>
                <!-- <a-button style="margin-left: 10px;">
                    Cancel
                </a-button> -->
            </a-form-model-item>
        </a-form-model>
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
    title: 'Plan 1: Selecting the dataset which store in Server',
    content: 'If you want to use the Server dataset you can watch "Select datases" areas instead switching open the bottom of "Update by yourself,'
  },
  {
    title: 'Plan 2: Updateing the datase by yourself',
    content: 'If you want to use yourself dataset, you can switch open the bottom and update your data, and then choose the dataset type you updated'
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
        desc: '',
        disabled1: true,
        disabled2: false
      },
      ListData
    }
  },
  methods: {
    handleClick () {
      this.loading = !this.loading
    },
    onSubmit () {
      console.log(this.current)
      this.current += 1
      this.$emit('changeCurrent', this.current)
    },
    handleChange () {
      if (this.form.delivery === true) {
        this.form.disabled1 = false
        this.form.disabled2 = true
      } else {
        this.form.disabled1 = true
        this.form.disabled2 = false
      }
    }
  }
}
</script>
