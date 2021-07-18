<template>
  <div >
    <a-card :loading="loading" title="Pre-processing recording" >
    <a-card-grid style="width:30%;text-align:center">
      <h3> Pre-processing recording description </h3>
      <a-list item-layout="horizontal" :data-source="ListData">
        <a-list-item slot="renderItem" slot-scope="item">
          <a-list-item-meta :description= "item.content">
            <a slot="title">{{ item.title }}</a>
          </a-list-item-meta>
        </a-list-item>
      </a-list>
    </a-card-grid>
    <a-card-grid style="width:70%" :hoverable="false">
      <h3>  Please choose the type of the pre-processing if you want </h3>
      <br><br>
              <a-collapse accordion>
                <a-collapse-panel key="1" header="Bandpass Filter">
                  <a-form-model :model="form" :label-col="labelCol" :wrapper-col="wrapperCol">
                      <a-form-model-item label="BandPass Filter: ">
                        <a-switch v-model="form.bandPass_filter" />
                      </a-form-model-item>
                    <a-tooltip placement="topLeft" title="High-pass cutoff frequency" arrow-point-at-center>
                      <a-form-model-item label="Freq_min: ">
                        <a-input v-model="form.freq_min" placeholder="Default value is 300" />
                      </a-form-model-item>
                    </a-tooltip>
                     <a-tooltip placement="topLeft" title="Low-pass cutoff frequency" arrow-point-at-center>
                      <a-form-model-item label="Freq_max: ">
                        <a-input v-model="form.freq_max" placeholder="Default value is 6000" />
                      </a-form-model-item>
                     </a-tooltip>
                    <a-tooltip placement="topLeft" title="Width of the filter (when type is ‘fft’)" arrow-point-at-center>
                      <a-form-model-item label="Freq_wid: ">
                        <a-input v-model="form.freq_wid" placeholder="Default value is 1000" />
                      </a-form-model-item>
                    </a-tooltip>
                    <a-tooltip placement="topLeft" title="The ‘fft’ filter uses a kernel in the frequency domain. The ‘butter’ filter uses scipy butter and filtfilt functions" arrow-point-at-center>
                      <a-form-model-item label="Filter Type">
                        <a-select v-model="form.filter_type" placeholder="Default type is 'fft' ">
                          <a-select-option value="fft">
                            fft
                          </a-select-option>
                          <a-select-option value="butter">
                            butter
                          </a-select-option>
                        </a-select>
                      </a-form-model-item>
                    </a-tooltip>
                    <a-tooltip placement="topLeft" title="Order of the filter (if ‘butter’)" arrow-point-at-center>
                      <a-form-model-item label="Order: ">
                        <a-input v-model="form.order" placeholder="Default value is 3" />
                      </a-form-model-item>
                    </a-tooltip>
                     <a-tooltip placement="topLeft" title="The chunk size to be used for the filtering" arrow-point-at-center>
                      <a-form-model-item label="Chunk Size: ">
                        <a-input v-model="form.chunk_size" placeholder="Default value is 300" />
                      </a-form-model-item>
                     </a-tooltip>
                  </a-form-model>
                </a-collapse-panel>
                <a-collapse-panel key="2" header="Notch Filter">
                  <a-form-model :model="form1" :label-col="labelCol" :wrapper-col="wrapperCol">
                    <a-form-model-item label="Notch Filter: ">
                      <a-switch v-model="form1.notch_filter" />
                    </a-form-model-item>
                    <a-tooltip placement="topLeft" title="The target frequency of the notch filter" arrow-point-at-center>
                      <a-form-model-item label="Freq: ">
                        <a-input v-model="form1.freq" placeholder="Default value is 3000" />
                      </a-form-model-item>
                    </a-tooltip>
                    <a-tooltip placement="topLeft" title="The quality factor of the notch filter" arrow-point-at-center>
                      <a-form-model-item label="q">
                        <a-input v-model="form1.q" placeholder="Default value is 30" />
                      </a-form-model-item>
                    </a-tooltip>
                    <a-tooltip placement="topLeft" title="The chunk size to be used for the filtering" arrow-point-at-center>
                      <a-form-model-item label="Chunk Size: ">
                        <a-input v-model="form1.chunk_size" placeholder="Default value is 300" />
                      </a-form-model-item>
                    </a-tooltip>
                  </a-form-model>
                </a-collapse-panel>
                <a-collapse-panel key="3" header="Remove Bad Channels">
                  <a-form-model :model="form2" :label-col="labelCol" :wrapper-col="wrapperCol">
                    <a-form-model-item label="Remove Bad Channels: ">
                      <a-switch v-model="form2.remove_bad_channels" />
                    </a-form-model-item>
                    <a-tooltip placement="topLeft" title="List of bad channel ids (int). If None, automatic removal will be done based on standard deviation" arrow-point-at-center>
                      <a-form-model-item label="Bad Channel Ids: ">
                        <a-input v-model="form2.bad_channel_ids" placeholder="Default value is None, the type is list" />
                      </a-form-model-item>
                    </a-tooltip>
                    <a-tooltip placement="topLeft" title="If automatic is used, the threshold for the standard deviation over which channels are removed" arrow-point-at-center>
                      <a-form-model-item label="bad_threshold">
                        <a-input v-model="form2.bad_threshold" placeholder="Default value is 2" />
                      </a-form-model-item>
                    </a-tooltip>
                    <a-tooltip placement="topLeft" title="If automatic is used, the number of seconds used to compute standard deviations" arrow-point-at-center>
                      <a-form-model-item label="seconds: ">
                        <a-input v-model="form2.seconds" placeholder="Default value is 10" />
                      </a-form-model-item>
                    </a-tooltip>
                    <a-tooltip placement="topLeft" title="If True, output is verbose" arrow-point-at-center>
                      <a-form-model-item label="Verbose: ">
                        <a-switch v-model="form2.verbose" />
                      </a-form-model-item>
                    </a-tooltip>
                  </a-form-model>
                </a-collapse-panel>
                <a-collapse-panel key="4" header="Transform">
                  <a-form-model :model="form3" :label-col="labelCol" :wrapper-col="wrapperCol">
                    <a-form-model-item label="Remove Bad Channels: ">
                      <a-switch v-model="form3.transform" />
                    </a-form-model-item>
                    <a-tooltip placement="topLeft" title="Scalar for the traces of the recording extractor or array with scalars for each channel" arrow-point-at-center>
                      <a-form-model-item label="Scale: ">
                        <a-input v-model="form3.scale" placeholder="Default value is 1" />
                      </a-form-model-item>
                    </a-tooltip>
                    <a-tooltip placement="topLeft" title="Offset for the traces of the recording extractor or array with offsets for each channel" arrow-point-at-center>
                      <a-form-model-item label="Offset:">
                        <a-input v-model="form3.offset" placeholder="Default value is 0" />
                      </a-form-model-item>
                    </a-tooltip>
                  </a-form-model>
                </a-collapse-panel>
                <a-collapse-panel key="5" header="Resample">
                  <a-form-model :model="form4" :label-col="labelCol" :wrapper-col="wrapperCol">
                    <a-form-model-item label="Resample: ">
                      <a-switch v-model="form4.resample" />
                    </a-form-model-item>
                    <a-tooltip placement="topLeft" title="The resample recording extractor" arrow-point-at-center>
                        <a-form-model-item label="Resample_rate:">
                          <a-input v-model="form4.resample_rate" placeholder="Default value is 0" />
                        </a-form-model-item>
                      </a-tooltip>
                    </a-form-model>
                </a-collapse-panel>
              </a-collapse>
        <br><br>
        <a-form-model>
          <a-form-model-item :wrapper-col="{ span:100, offset: 100 }">
            <a-button type="primary" @click="onSubmit">
              Confirm
            </a-button>
            <!-- <a-button style="margin-left: 10px;">
              Next One
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
    title: 'Bandpass Filter',
    content: 'Performs a lazy filter on the recording extractor traces.'
  },
  {
    title: 'Notch Filter',
    content: 'Performs a notch filter on the recording extractor traces using scipy iirnotch function'
  },
  {
    title: 'Remove Bad Channels',
    content: 'Remove bad channels from the recording extractor'
  },
  {
    title: 'Transform',
    content: 'Transforms the traces from the given recording extractor with a scalar and offset. New traces = traces*scalar + offset'
  },
  {
    title: 'Resample',
    content: 'Resamples the recording extractor traces. If the resampling rate is multiple of the sampling rate, the faster scipy decimate function is used'
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
        bandPass_filter: false,
        freq_min: '',
        freq_max: '',
        freq_wid: '',
        filter_type: '',
        order: '',
        chunk_size: ''
      },
      form1: {
        notch_filter: false,
        freq: '',
        q: '',
        chunk_size: ''
      },
      form2: {
        remove_bad_channels: false,
        bad_channel_ids: '',
        bad_threshold: '',
        seconds: '',
        verbose: false
      },
      form3: {
        transform: false,
        scale: '',
        offset: ''
      },
      form4: {
        resample: false,
        resample_rate: ''
      },
      ListData
    }
  },
  methods: {
    handleClick () {
      this.loading = !this.loading
    },
    onSubmit () {
      if (this.form.bandPass_filter === true) {
        if (this.form.freq_min === '') {
          this.form.freq_min = 300
        }
        if (this.form.freq_max === '') {
          this.form.freq_max = 6000
        }
        if (this.form.freq_wid === '') {
          this.form.freq_wid = 1000
        }
        if (this.form.filter_type === '') {
          this.form.filter_type = 'fft'
        }
        if (this.form.order === '') {
          this.form.order = 3
        }
        if (this.form.chunk_size === '') {
          this.form.chunk_size = 300
        }
        console.log('submit bandpass filter', this.form)
      }
      if (this.form1.notch_filter === true) {
        if (this.form1.freq === '') {
          this.form1.freq = 3000
        }
        if (this.form1.q === '') {
          this.form1.q = 30
        }
        if (this.form1.chunk_size === '') {
          this.form1.chunk_size = 300
        }
        console.log('submit notch filter', this.form1)
      }
      if (this.form2.remove_bad_channels === true) {
        if (this.form2.bad_channel_ids === '') {
          this.form2.bad_channel_ids = 'None'
        }
        if (this.form2.bad_threshold === '') {
          this.form2.bad_threshold = 2
        }
        if (this.form2.seconds === '') {
          this.form2.seconds = 10
        }
        console.log('submit bad channels', this.form2)
      }
      if (this.form3.transform === true) {
        if (this.form3.scale === '') {
          this.form3.scale = 1
        }
        if (this.form3.offset === '') {
          this.form3.offset = 0
        }
        console.log('submit transform', this.form3)
      }
      if (this.form4.resample === true) {
        if (this.form4.resample_rate === '') {
          this.form4.resample_rate = 0
        }
        console.log('submit resample', this.form4)
      }
      console.log(this.current)
      this.current += 1
      this.$emit('changeCurrent', this.current)
    }
  }
}
</script>
