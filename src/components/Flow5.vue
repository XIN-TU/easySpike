-01<template>
  <div >
    <a-card :loading="loading" title="Validation" >
    <a-card-grid style="width:30%;text-align:center">
      <h3> Validation description </h3>
      <a-list item-layout="horizontal" :data-source="ListData">
        <a-list-item slot="renderItem" slot-scope="item">
          <a-list-item-meta :description= "item.content">
            <a slot="title">{{ item.title }}</a>
          </a-list-item-meta>
        </a-list-item>
      </a-list>
    </a-card-grid>
    <a-card-grid style="width:70%" :hoverable="false">
      <h3>  Please choose the type of the Validation way and its paramters if you want </h3>
      <br>
              <a-collapse accordion>
                <a-collapse-panel key="1" header="Compute isi Violations">
                  <a-form-model :model="form" :label-col="labelCol" :wrapper-col="wrapperCol">
                    <a-form-model-item label="Compute isi Violations">
                        <a-switch v-model="form.compute_isi_violations" />
                      </a-form-model-item>
                     <a-tooltip placement="topLeft" title="" arrow-point-at-center>
                      <a-form-model-item label="isi Threshold ms">
                        <a-input v-model="form.isi_threshold_ms" placeholder="Default is 1.5" />
                      </a-form-model-item>
                     </a-tooltip>
                  </a-form-model>
                </a-collapse-panel>
                <a-collapse-panel key="2" header="Compute snrs">
                  <a-form-model :model="form1" :label-col="labelCol" :wrapper-col="wrapperCol">
                      <a-form-model-item label="Compute Snrs">
                        <a-switch v-model="form1.compute_snrs" />
                      </a-form-model-item>
                     <a-tooltip placement="topLeft" title="" arrow-point-at-center>
                      <a-form-model-item label="Peak Sign">
                        <a-input v-model="form1.peak_sign" placeholder="Default is neg" />
                      </a-form-model-item>
                     </a-tooltip>
                  </a-form-model>
                </a-collapse-panel>
                <a-collapse-panel key="3" header="Compute Num Spikes" >
                  <a-form-model :model="form" :label-col="labelCol" :wrapper-col="wrapperCol">
                      <a-form-model-item label="Compute Num Spikes">
                        <a-switch v-model="form.compute_num_spikes" />
                      </a-form-model-item>
                  </a-form-model>
                </a-collapse-panel>
                <a-collapse-panel key="4" header="Compute Firing Rate">
                  <a-form-model :model="form3" :label-col="labelCol" :wrapper-col="wrapperCol">
                      <a-form-model-item label="Compute Firing Rate">
                        <a-switch v-model="form3.compute_firing_rate" />
                      </a-form-model-item>
                  </a-form-model>
                </a-collapse-panel>
                <a-collapse-panel key="5" header="Compute Presence Ratio">
                  <a-form-model :model="form4" :label-col="labelCol" :wrapper-col="wrapperCol">
                      <a-form-model-item label="Compute Presence Ratio">
                        <a-switch v-model="form4.compute_presence_ratio" />
                      </a-form-model-item>
                     <a-tooltip placement="topLeft" title="" arrow-point-at-center>
                      <a-form-model-item label="Num Bin Edges">
                        <a-input v-model="form4.num_bin_edges" placeholder="Default is 101" />
                      </a-form-model-item>
                     </a-tooltip>
                  </a-form-model>
                </a-collapse-panel>
                <a-collapse-panel key="6" header="Compute Amplitudes Cutoff">
                  <a-form-model :model="form5" :label-col="labelCol" :wrapper-col="wrapperCol">
                      <a-form-model-item label="Compute Amplitudes Cutoff">
                        <a-switch v-model="form5.compute_amplitudes_cutoff" />
                      </a-form-model-item>
                     <a-tooltip placement="topLeft" title="" arrow-point-at-center>
                      <a-form-model-item label="Peak Sign">
                        <a-input v-model="form5.peak_sign" placeholder="Default is neg" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="" arrow-point-at-center>
                      <a-form-model-item label="Num Histogram Bins">
                        <a-input v-model="form5.num_histogram_bins" placeholder="Default is 500" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="" arrow-point-at-center>
                      <a-form-model-item label="Histogram Smoothing Value">
                        <a-input v-model="form5.histogram_smoothing_value" placeholder="Default is 3" />
                      </a-form-model-item>
                     </a-tooltip>
                  </a-form-model>
                </a-collapse-panel>
              </a-collapse>
        <br>
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
    title: 'Compute isi Violations',
    content: 'Computes and returns the isi violations for the sorted dataset'
  },
  {
    title: 'Compute snrs ',
    content: 'Compute signal to noise ratio'
  },
  {
    title: 'compute_num_spikes',
    content: 'Compute number of spike accross segments'
  },
  {
    title: 'compute_firing_rate',
    content: 'Compute firing rate acrros segments'
  },
  {
    title: 'compute_presence_ratio',
    content: 'Calculate fraction of time the unit is is firing for epochs'
  },
  {
    title: 'compute_amplitudes_cutoff',
    content: 'Calculate approximate fraction of spikes missing from a distribution of amplitudes'
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
        compute_isi_violations: false,
        isi_threshold_ms: ''
      },
      form1: {
        compute_snrs: false,
        peak_sign: ''
      },
      form2: {
        compute_num_spikes: false
      },
      form3: {
        compute_firing_rate: false
      },
      form4: {
        compute_presence_ratio: false,
        num_bin_edges: ''
      },
      form5: {
        compute_amplitudes_cutoff: false,
        peak_sign: '',
        num_histogram_bins: '',
        histogram_smoothing_value: ''
      },
      ListData
    }
  },
  methods: {
    handleClick () {
      this.loading = !this.loading
    },
    onSubmit () {
      if (this.form.compute_isi_violations === true) {
        if (this.form.isi_threshold_ms === '') {
          this.form.isi_threshold_ms = 1.5
        }
        console.log('submit! compute_isi_violations', this.form)
      }
      if (this.form.compute_snrs === true) {
        if (this.form1.compute_snrs === '') {
          this.form1.compute_snrs = 'neg'
        }
        console.log('submit! compute_snrs', this.form1)
      }
      if (this.form2.compute_num_spikes === true) {
        console.log('submit! compute_num_spikes', this.form2)
      }
      if (this.form3.compute_firing_rate === true) {
        console.log('submit! compute_firing_rate', this.form3)
      }
      if (this.form4.compute_presence_ratio === true) {
        if (this.form4.num_bin_edges === '') {
          this.form4.num_bin_edges = 101
        }
        console.log('submit! compute_presence_ratio', this.form4)
      }
      if (this.form5.compute_amplitudes_cutoff === true) {
        if (this.form5.peak_sign === '') {
          this.form5.peak_sign = 'neg'
        }
        if (this.form5.num_histogram_bins === '') {
          this.form5.num_histogram_bins = 500
        }
        if (this.form5.histogram_smoothing_value === '') {
          this.form5.histogram_smoothing_value = 3
        }
        console.log('submit! compute_amplitudes_cutoff', this.form5)
      }
      this.current += 1
      this.$emit('changeCurrent', this.current)
    }
  }
}
</script>
