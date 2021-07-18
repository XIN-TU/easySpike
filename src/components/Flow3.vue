<template>
  <div >
    <a-card :loading="loading" title="Spike Sorting" >
    <a-card-grid style="width:30%;text-align:center">
      <h3> Spike sorting sorter description </h3>
      <a-list item-layout="horizontal" :data-source="ListData">
        <a-list-item slot="renderItem" slot-scope="item">
          <a-list-item-meta :description= "item.content">
            <a slot="title">{{ item.title }}</a>
          </a-list-item-meta>
        </a-list-item>
      </a-list>
    </a-card-grid>
    <a-card-grid style="width:70%" :hoverable="false">
      <h3>  Please choose the type of the sorter and its paramters if you want </h3>
      <br>
      <a-select style="width: 100%" placeholder="Please choose the sorter" @change="handleChange">
        <a-select-option value='klusta'>klusta</a-select-option>
        <a-select-option value='herdingspikes'>herdingspikes</a-select-option>
        <a-select-option value='tridesclous'>tridesclous</a-select-option>
      </a-select>
      <br><br>
              <a-collapse accordion>
                <a-collapse-panel key="1" header="Klusta" :disabled = 'disable1'>
                  <a-form-model :model="form" :label-col="labelCol" :wrapper-col="wrapperCol">
                     <a-tooltip placement="topLeft" title="Radius in um to build channel neighborhood" arrow-point-at-center>
                      <a-form-model-item label="Adjacency Radius: ">
                        <a-input v-model="form.adjacency_radius" placeholder="Default is None" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Strong threshold for spike detection" arrow-point-at-center>
                      <a-form-model-item label="Threshold Strong Std Factor : ">
                        <a-input v-model="form.threshold_strong_std_factor" placeholder="Default is 5" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Weak threshold for spike detection" arrow-point-at-center>
                      <a-form-model-item label="Threshold Weak Std Factor : ">
                        <a-input v-model="form.threshold_weak_std_factor" placeholder="Default is 2" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Use -1 (negative), 1 (positive) or 0 (both) depending on the sign of the spikes in the recording" arrow-point-at-center>
                      <a-form-model-item label="Detect Sign : ">
                        <a-input v-model="form.detect_sign" placeholder="Default is -1" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Number of samples to cut out before the peak" arrow-point-at-center>
                      <a-form-model-item label="Extracts Before: ">
                        <a-input v-model="form.extract_s_before" placeholder="Default is 16" />
                      </a-form-model-item>
                     </a-tooltip>
                      <a-tooltip placement="topLeft" title="Number of samples to cut out after the peak" arrow-point-at-center>
                      <a-form-model-item label="Extracts After: ">
                        <a-input v-model="form.extract_s_after" placeholder="Default is 32" />
                      </a-form-model-item>
                      </a-tooltip>
                      <a-tooltip placement="topLeft" title="Number of PCA features per channel" arrow-point-at-center>
                      <a-form-model-item label="n Features Per Channel: ">
                        <a-input v-model="form.n_features_per_channel" placeholder="Default is 3" />
                      </a-form-model-item>
                     </a-tooltip>
                      <a-tooltip placement="topLeft" title="Maximum number of waveforms for PCA" arrow-point-at-center>
                      <a-form-model-item label="PCA n Waveforms Max ">
                        <a-input v-model="form.pca_n_waveforms_max" placeholder="Default is 10000" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Number of initial clusters" arrow-point-at-center>
                      <a-form-model-item label="Num Starting Clusters ">
                        <a-input v-model="form.num_starting_clusters" placeholder="Default is 50" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Chunk size in Mb for saving to binary format (default 500Mb)" arrow-point-at-center>
                      <a-form-model-item label="Total Memory">
                        <a-input v-model="form.total_memory" placeholder="Default is 500M" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Number of jobs for saving to binary format (Default 1)" arrow-point-at-center>
                      <a-form-model-item label="n Jobs Bin">
                        <a-input v-model="form.n_jobs_bin" placeholder="Default is 1" />
                      </a-form-model-item>
                     </a-tooltip>
                  </a-form-model>
                </a-collapse-panel>
                <a-collapse-panel key="2" header="Herdingspikes" :disabled = 'disable2'>
                  <a-form-model :model="form1" :label-col="labelCol" :wrapper-col="wrapperCol">
                    <a-tooltip placement="topLeft" title="Meanshift bandwidth, average spatiel extent of spike clusters (um)" arrow-point-at-center>
                      <a-form-model-item label="Clustering BandWidth">
                        <a-input v-model="form1.clustering_bandwidth" placeholder="Default is 5.5" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Scalar for the waveform PC features when clustering" arrow-point-at-center>
                      <a-form-model-item label="Clustering Alpha">
                        <a-input v-model="form1.clustering_alpha" placeholder="Default is 5.5" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Number of cores to use for clustering" arrow-point-at-center>
                      <a-form-model-item label="Clustering n Jobs">
                        <a-input v-model="form1.clustering_n_jobs" placeholder="Default is -1" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Enable clustering bin seeding" arrow-point-at-center>
                      <a-form-model-item label="Clustering Bin Seeding">
                        <a-switch v-model="form1.clustering_bin_seeding" defaultChecked/>
                        <!-- 默认参数是True 但是不知道能开关变成打开 -->
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Minimum spikes per bin for bin seeding" arrow-point-at-center>
                      <a-form-model-item label="Clustering min bin Freq">
                        <a-input v-model="form1.clustering_min_bin_freq" placeholder="Default is 16" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Number of spikes used to build clusters. All by default" arrow-point-at-center>
                      <a-form-model-item label="Clustering Subset">
                        <a-input v-model="form1.clustering_subset" placeholder="Default is None" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Cutout size before peak (ms)" arrow-point-at-center>
                      <a-form-model-item label="Left Cutout Time">
                        <a-input v-model="form1.left_cutout_time" placeholder="Default is 0.3" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Cutout size after peak (ms)" arrow-point-at-center>
                      <a-form-model-item label="Right Cutout Time">
                        <a-input v-model="form1.right_cutout_time" placeholder="Default is 1.8" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Detection threshold" arrow-point-at-center>
                      <a-form-model-item label="Detect Threshold">
                        <a-input v-model="form1.detect_threshold" placeholder="Default is 20" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Masked channels" arrow-point-at-center>
                      <a-form-model-item label="Probe Masked Channels">
                        <a-input v-model="form1.probe_masked_channels" placeholder="Default is []" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Radius of area around probe channel for localization" arrow-point-at-center>
                      <a-form-model-item label="Probe Inner Radius">
                        <a-input v-model="form1.probe_inner_radius" placeholder="Default is 70" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Radius of area around probe channel for neighbor classification" arrow-point-at-center>
                      <a-form-model-item label="Probe Neighbor Radius">
                        <a-input v-model="form1.probe_neighbor_radius" placeholder="Default is 90" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Duration of a spike event (ms)" arrow-point-at-center>
                      <a-form-model-item label="Probe Event Length">
                        <a-input v-model="form1.probe_event_length" placeholder="Default is 0.26" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Maxmimum peak misalignment for synchronous spike (ms)" arrow-point-at-center>
                      <a-form-model-item label="Probe Peak Jitter">
                        <a-input v-model="form1.probe_peak_jitter" placeholder="Default is 0.2" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="" arrow-point-at-center>
                      <a-form-model-item label="t Inc">
                        <a-input v-model="form1.t_inc" placeholder="Default is 100000" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Number of centroids to average when localizing" arrow-point-at-center>
                      <a-form-model-item label="Num Com Centers">
                        <a-input v-model="form1.num_com_centers" placeholder="Default is 1" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Minimum summed spike amplitude for spike acceptance" arrow-point-at-center>
                      <a-form-model-item label="maa">
                        <a-input v-model="form1.maa" placeholder="Default is 12" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Requires magnitude of spike rebound for acceptance" arrow-point-at-center>
                      <a-form-model-item label="Ahpthr">
                        <a-input v-model="form1.ahpthr" placeholder="Default is 11" />
                      </a-form-model-item>
                     </a-tooltip>
                     <!-- <a-tooltip placement="topLeft" title="File name for storage of unclustered detected spikes" arrow-point-at-center>
                      <a-form-model-item label="Out File Name">
                        <a-input v-model="form1.out_file_name" placeholder="Default is HS2_detected" />
                      </a-form-model-item>
                     </a-tooltip> -->
                     <a-tooltip placement="topLeft" title="Experimental: Set to True at your risk" arrow-point-at-center>
                      <a-form-model-item label="Decay Filtering">
                        <a-switch v-model="form1.decay_filtering" />
                      </a-form-model-item>
                     </a-tooltip>
                     <!-- <a-tooltip placement="topLeft" title="Save all working files after sorting (slow)" arrow-point-at-center>
                      <a-form-model-item label="Save All">
                        <a-switch v-model="form1.save_all" />
                      </a-form-model-item>
                     </a-tooltip> -->
                     <a-tooltip placement="topLeft" title="Amplitude evaluation time (ms)" arrow-point-at-center>
                      <a-form-model-item label="Amp Evaluation Time">
                        <a-input v-model="form1.amp_evaluation_time" placeholder="Default is 0.4" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Spike evaluation time (ms)" arrow-point-at-center>
                      <a-form-model-item label="Spk Evaluation Time">
                        <a-input v-model="form1.spk_evaluation_time" placeholder="Default is 1.0" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Number of principal components to use when clustering" arrow-point-at-center>
                      <a-form-model-item label="PCA ncomponents">
                        <a-input v-model="form1.pca_ncomponents" placeholder="Default is 2" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="If true, whiten data for pca" arrow-point-at-center>
                      <a-form-model-item label="pca_whiten">
                        <a-switch v-model="form1.pca_whiten" defaultChecked/>
                        <!-- 默认参数是True 但是不知道能开关变成打开 -->
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="High-pass filter cutoff frequency" arrow-point-at-center>
                      <a-form-model-item label="Freq Min">
                        <a-input v-model="form1.freq_min" placeholder="Default is 300" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Low-pass filter cutoff frequency" arrow-point-at-center>
                      <a-form-model-item label="Freq Max">
                        <a-input v-model="form1.freq_max" placeholder="Default is 6000" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Enable or disable filter" arrow-point-at-center>
                      <a-form-model-item label="Filter">
                        <a-switch v-model="form1.filter" defaultChecked/>
                        <!-- 默认参数是True 但是不知道能开关变成打开 -->
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Scales recording traces to optimize HerdingSpikes performance" arrow-point-at-center>
                      <a-form-model-item label="Pre Scale">
                        <a-switch v-model="form.pre_scale" defaultChecked/>
                        <!-- 默认参数是True 但是不知道能开关变成打开 -->
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Scale to apply in case of pre-scaling of traces" arrow-point-at-center>
                      <a-form-model-item label="Pre Scale Value ">
                        <a-input v-model="form.pre_scale_value" placeholder="Default is 20" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Remove spike duplicates (based on spk_evaluation_time)" arrow-point-at-center>
                      <a-form-model-item label="Filter Duplicates">
                        <a-switch v-model="form.filter_duplicates" defaultChecked/>
                        <!-- 默认参数是True 但是不知道能开关变成打开 -->
                      </a-form-model-item>
                     </a-tooltip>
                  </a-form-model>
                </a-collapse-panel>
                <a-collapse-panel key="3" header="tridesclous" :disabled = 'disable3'>
                  <a-form-model :model="form2" :label-col="labelCol" :wrapper-col="wrapperCol">
                      <a-tooltip placement="topLeft" title="remove common reference with median" arrow-point-at-center>
                      <a-form-model-item label="Common Ref Removal">
                        <a-switch v-model="form2.common_ref_removal" />
                      </a-form-model-item>
                    </a-tooltip>
                      <a-tooltip placement="topLeft" title="High-pass filter cutoff frequency" arrow-point-at-center>
                      <a-form-model-item label="Freq Min ">
                        <a-input v-model="form2.freq_min" placeholder="Default is 400" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Low-pass filter cutoff frequency" arrow-point-at-center>
                      <a-form-model-item label="Freq Max ">
                        <a-input v-model="form2.freq_max" placeholder="Default is 5000" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Use -1 (negative) or 1 (positive) depending on the sign of the spikes in the recording" arrow-point-at-center>
                      <a-form-model-item label="Detect Sign ">
                        <a-input v-model="form2.detect_sign" placeholder="Default is -1" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Threshold for spike detection" arrow-point-at-center>
                      <a-form-model-item label="Detect Threshold">
                        <a-input v-model="form2.detect_threshold" placeholder="Default is 5" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="" arrow-point-at-center>
                      <a-form-model-item label="Nested Params">
                        <a-input v-model="form2.nested_params" placeholder="Default is None" />
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
    title: 'Klusta',
    content: 'Klusta is a density-based spike sorter that uses a masked EM approach for clustering For more information see https://doi.org/10.1038/nn.4268 '
  },
  {
    title: 'Herdingspikes ',
    content: 'Herding Spikes is a density-based spike sorter designed for high-density retinal recordings.It uses both PCA features and an estimate of the spike location to cluster different units. For more information see https://doi.org/10.1016/j.jneumeth.2016.06.006 '
  },
  {
    title: 'Tridesclous',
    content: 'Tridesclous is a template-matching spike sorter with a real-time engine. For more information see https://tridesclous.readthedocs.io '
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
        adjacency_radius: '',
        threshold_strong_std_factor: '',
        threshold_weak_std_factor: '',
        detect_sign: '',
        extract_s_before: '',
        extract_s_after: '',
        n_features_per_channel: '',
        pca_n_waveforms_max: '',
        num_starting_clusters: '',
        total_memory: '',
        n_jobs_bin: ''
      },
      form1: {
        clustering_bandwidth: '',
        clustering_alpha: '',
        clustering_n_jobs: '',
        clustering_bin_seeding: true,
        clustering_min_bin_freq: '',
        clustering_subset: '',
        left_cutout_time: '',
        right_cutout_time: '',
        detect_threshold: '',
        probe_masked_channels: '',
        probe_inner_radius: '',
        probe_neighbor_radius: '',
        probe_event_length: '',
        probe_peak_jitter: '',
        t_inc: '',
        num_com_centers: '',
        maa: '',
        ahpthr: '',
        // out_file_name: 'HS2_detected',
        decay_filtering: false,
        // save_all: false,
        amp_evaluation_time: '',
        spk_evaluation_time: '',
        pca_ncomponents: '',
        pca_whiten: true,
        freq_min: '',
        freq_max: '',
        filter: true,
        pre_scale: true,
        pre_scale_value: '',
        filter_duplicates: true

      },
      form2: {
        freq_min: '',
        freq_max: '',
        detect_sign: '',
        detect_threshold: '',
        common_ref_removal: false,
        nested_params: ''
      },
      ListData,
      disable1: true,
      disable2: true,
      disable3: true,
      sorterType: ''
    }
  },
  methods: {
    handleClick () {
      this.loading = !this.loading
    },
    onSubmit () {
      console.log(this.sorterType)
      switch (this.sorterType) {
        case 'klusta':
          if (this.form.adjacency_radius === '') {
            this.form.adjacency_radius = 'None'
          }
          if (this.form.threshold_strong_std_factor === '') {
            this.form.threshold_strong_std_factor = 5
          }
          if (this.form.threshold_weak_std_factor === '') {
            this.form.threshold_weak_std_factor = 2
          }
          if (this.form.detect_sign === '') {
            this.form.detect_sign = -1
          }
          if (this.form.extract_s_before === '') {
            this.form.extract_s_before = 16
          }
          if (this.form.extract_s_after === '') {
            this.form.extract_s_after = 32
          }
          if (this.form.n_features_per_channel === '') {
            this.form.n_features_per_channel = 3
          }
          if (this.form.pca_n_waveforms_max === '') {
            this.form.pca_n_waveforms_max = 10000
          }
          if (this.form.num_starting_clusters === '') {
            this.form.num_starting_clusters = 50
          }
          if (this.form.total_memory === '') {
            this.form.total_memory = '500M'
          }
          if (this.form.n_jobs_bin === '') {
            this.form.n_jobs_bin = 1
          }
          console.log('submit klusta', this.form)
          break
        case 'herdingspikes':
          if (this.form1.clustering_bandwidth === '') {
            this.form1.clustering_bandwidth = 5.5
          }
          if (this.form1.clustering_alpha === '') {
            this.form1.clustering_alpha = 5.5
          }
          if (this.form1.clustering_n_jobs === '') {
            this.form1.clustering_n_jobs = -1
          }
          if (this.form1.clustering_min_bin_freq === '') {
            this.form1.clustering_min_bin_freq = 16
          }
          if (this.form1.clustering_subset === '') {
            this.form1.clustering_subset = 'None'
          }
          if (this.form1.left_cutout_time === '') {
            this.form1.left_cutout_time = 0.3
          }
          if (this.form1.right_cutout_time === '') {
            this.form1.right_cutout_time = 1.8
          }
          if (this.form1.detect_threshold === '') {
            this.form1.detect_threshold = 20
          }
          if (this.form1.probe_masked_channels === '') {
            this.form1.probe_masked_channels = '[]'
          }
          if (this.form1.probe_inner_radius === '') {
            this.form1.probe_inner_radius = 70
          }
          if (this.form1.probe_neighbor_radius === '') {
            this.form1.probe_neighbor_radius = 90
          }
          if (this.form1.probe_event_length === '') {
            this.form1.probe_event_length = 0.26
          }
          if (this.form1.probe_peak_jitter === '') {
            this.form1.probe_peak_jitter = 0.2
          }
          if (this.form1.t_inc === '') {
            this.form1.t_inc = 100000
          }
          if (this.form1.num_com_centers === '') {
            this.form1.num_com_centers = 1
          }
          if (this.form1.maa === '') {
            this.form1.maa = 12
          }
          if (this.form1.ahpthr === '') {
            this.form1.ahpthr = 11
          }
          if (this.form1.amp_evaluation_time === '') {
            this.form1.amp_evaluation_time = 0.4
          }
          if (this.form1.spk_evaluation_time === '') {
            this.form1.spk_evaluation_time = 1
          }
          if (this.form1.pca_ncomponents === '') {
            this.form1.pca_ncomponents = 2
          }
          if (this.form1.freq_min === '') {
            this.form1.freq_min = 300
          }
          if (this.form1.freq_max === '') {
            this.form1.freq_max = 6000
          }
          if (this.form1.pre_scale_value === '') {
            this.form1.pre_scale_value = 20
          }
          console.log('submit herdingspikes', this.form1)
          break
        case 'tridesclous':
          if (this.form2.freq_min === '') {
            this.form2.freq_min = 400
          }
          if (this.form2.freq_max === '') {
            this.form2.freq_max = 5000
          }
          if (this.form2.detect_sign === '') {
            this.form2.detect_sign = -1
          }
          if (this.form2.detect_threshold === '') {
            this.form2.detect_threshold = 5
          }
          if (this.form2.nested_params === '') {
            this.form2.nested_params = 'None'
          }
          console.log('submit tridesclous', this.form2)
          break
      }
      console.log(this.current)
      this.current += 1
      this.$emit('changeCurrent', this.current)
    },
    handleChange (value) {
      console.log(`selected ${value}`)
      this.sorterType = value
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
    }
  }
}
</script>
