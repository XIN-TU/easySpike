<template>
  <div >
    <a-card :loading="loading" title="Post-processing recording" >
    <a-card-grid style="width:30%;text-align:center">
      <h3> Post-processing recording description </h3>
      <a-list item-layout="horizontal" :data-source="ListData">
        <a-list-item slot="renderItem" slot-scope="item">
          <a-list-item-meta :description= "item.content">
            <a slot="title">{{ item.title }}</a>
          </a-list-item-meta>
        </a-list-item>
      </a-list>
    </a-card-grid>
    <a-card-grid style="width:70%" :hoverable="false">
      <h3>  Please choose the type of the post-processing if you want </h3>
      <br><br>
              <a-collapse accordion>
                <a-collapse-panel key="1" header="Get Unit Waveforms">
                  <a-form-model :model="form" :label-col="labelCol" :wrapper-col="wrapperCol">
                      <a-form-model-item label="Get Unit Waveforms">
                        <a-switch v-model="form.get_unit_waveforms" />
                      </a-form-model-item>
                      <a-tooltip placement="topLeft" title="The sorting extractor" arrow-point-at-center>
                      <a-form-model-item label="Sorting">
                        <a-select v-model="form.sorting" placeholder="Default type is 'fft' ">
                          <a-select-option value="fft">
                            fft
                          </a-select-option>
                          <a-select-option value="butter">
                            butter
                          </a-select-option>
                        </a-select>
                      </a-form-model-item>
                    </a-tooltip>
                     <a-tooltip placement="topLeft" title="List of unit ids to extract waveforms" arrow-point-at-center>
                      <a-form-model-item label="Unit Ids: ">
                        <a-input v-model="form.unit_ids" placeholder="Input List, default is None" />
                      </a-form-model-item>
                     </a-tooltip>
                    <a-tooltip placement="topLeft" title="List of channels ids to compute waveforms from" arrow-point-at-center>
                      <a-form-model-item label="Channel Ids ">
                        <a-input v-model="form.channel_ids" placeholder="Input List, default is None" />
                      </a-form-model-item>
                    </a-tooltip>
                    <a-tooltip placement="topLeft" title="If True, spike indexes and channel indexes are returned" arrow-point-at-center>
                      <a-form-model-item label="Return Idxs ">
                        <a-switch v-model="form.return_idxs" placeholder="Default is False"/>
                      </a-form-model-item>
                    </a-tooltip>
                    <a-tooltip placement="topLeft" title="Size of chunks in number of samples. If None, it is automatically calculated" arrow-point-at-center>
                      <a-form-model-item label="Chunk Size: ">
                        <a-input v-model="form.chunk_size" placeholder="Default value is None" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Size of chunks in Mb" arrow-point-at-center>
                      <a-form-model-item label="Chunk Mb: ">
                        <a-input v-model="form.chunk_mb" placeholder="Default value is 500" />
                      </a-form-model-item>
                     </a-tooltip>
                  </a-form-model>
                </a-collapse-panel>
                <a-collapse-panel key="2" header="Get Unit Templates">
                  <a-form-model :model="form1" :label-col="labelCol" :wrapper-col="wrapperCol">
                    <a-form-model-item label="Get Unit Templates">
                        <a-switch v-model="form1.get_unit_templates" />
                      </a-form-model-item>
                      <a-tooltip placement="topLeft" title="The sorting extractor" arrow-point-at-center>
                      <a-form-model-item label="Sorting">
                        <a-select v-model="form1.sorting" placeholder="Default type is 'fft' ">
                          <a-select-option value="fft">
                            fft
                          </a-select-option>
                          <a-select-option value="butter">
                            butter
                          </a-select-option>
                        </a-select>
                      </a-form-model-item>
                    </a-tooltip>
                     <a-tooltip placement="topLeft" title="List of unit ids to extract maximum channels" arrow-point-at-center>
                      <a-form-model-item label="Unit Ids: ">
                        <a-input v-model="form1.unit_ids" placeholder="Input List, default is None" />
                      </a-form-model-item>
                     </a-tooltip>
                    <a-tooltip placement="topLeft" title="List of channels ids to compute amplitudes from" arrow-point-at-center>
                      <a-form-model-item label="Channel Ids ">
                        <a-input v-model="form1.channel_ids" placeholder="Input List, default is None" />
                      </a-form-model-item>
                    </a-tooltip>
                    <a-tooltip placement="topLeft" title="Use ‘mean’ or ‘median’ to compute templates" arrow-point-at-center>
                      <a-form-model-item label="Mode">
                        <a-select v-model="form1.mode" placeholder="Default type is 'mean' ">
                          <a-select-option value="mean">
                            mean
                          </a-select-option>
                          <a-select-option value="Median">
                            Median
                          </a-select-option>
                        </a-select>
                      </a-form-model-item>
                    </a-tooltip>
                    <a-tooltip placement="topLeft" title="Size of chunks in number of samples. If None, it is automatically calculated" arrow-point-at-center>
                      <a-form-model-item label="Chunk Size: ">
                        <a-input v-model="form1.chunk_size" placeholder="Default value is None" />
                      </a-form-model-item>
                     </a-tooltip>
                  </a-form-model>
                </a-collapse-panel>
                <a-collapse-panel key="3" header="Get Unit Amplitudes">
                  <a-form-model :model="form2" :label-col="labelCol" :wrapper-col="wrapperCol">
                      <a-form-model-item label="Get Unit Amplitudes">
                        <a-switch v-model="form2.get_unit_amplitudes" />
                      </a-form-model-item>
                      <a-tooltip placement="topLeft" title="The sorting extractor" arrow-point-at-center>
                      <a-form-model-item label="Sorting">
                        <a-select v-model="form2.sorting" placeholder="Default type is 'fft' ">
                          <a-select-option value="fft">
                            fft
                          </a-select-option>
                          <a-select-option value="butter">
                            butter
                          </a-select-option>
                        </a-select>
                      </a-form-model-item>
                    </a-tooltip>
                     <a-tooltip placement="topLeft" title="List of unit ids to extract waveforms" arrow-point-at-center>
                      <a-form-model-item label="Unit Ids: ">
                        <a-input v-model="form2.unit_ids" placeholder="Input List, default is None" />
                      </a-form-model-item>
                     </a-tooltip>
                    <a-tooltip placement="topLeft" title="List of channels ids to compute waveforms from" arrow-point-at-center>
                      <a-form-model-item label="Channel Ids ">
                        <a-input v-model="form2.channel_ids" placeholder="Input List, default is None" />
                      </a-form-model-item>
                    </a-tooltip>
                    <a-tooltip placement="topLeft" title="If True, spike indexes and channel indexes are returned" arrow-point-at-center>
                      <a-form-model-item label="Return Idxs ">
                        <a-switch v-model="form2.return_idxs" placeholder="Default is False"/>
                      </a-form-model-item>
                    </a-tooltip>
                  </a-form-model>
                </a-collapse-panel>
                <a-collapse-panel key="4" header="Get Unit Max Channels">
                  <a-form-model :model="form3" :label-col="labelCol" :wrapper-col="wrapperCol">
                      <a-form-model-item label="Get Unit Max Channels">
                        <a-switch v-model="form3.get_unit_max_channels" />
                      </a-form-model-item>
                      <a-tooltip placement="topLeft" title="The sorting extractor" arrow-point-at-center>
                      <a-form-model-item label="Sorting">
                        <a-select v-model="form3.sorting" placeholder="Default type is 'fft' ">
                          <a-select-option value="fft">
                            fft
                          </a-select-option>
                          <a-select-option value="butter">
                            butter
                          </a-select-option>
                        </a-select>
                      </a-form-model-item>
                    </a-tooltip>
                     <a-tooltip placement="topLeft" title="List of unit ids to extract maximum channels" arrow-point-at-center>
                      <a-form-model-item label="Unit Ids: ">
                        <a-input v-model="form3.unit_ids" placeholder="Input List, default is None" />
                      </a-form-model-item>
                     </a-tooltip>
                    <a-tooltip placement="topLeft" title="List of channels ids to compute max_channels from" arrow-point-at-center>
                      <a-form-model-item label="Channel Ids ">
                        <a-input v-model="form3.channel_ids" placeholder="Input List, default is None" />
                      </a-form-model-item>
                    </a-tooltip>
                    <a-tooltip placement="topLeft" title="Number of max channels per units to return (default=1)" arrow-point-at-center>
                      <a-form-model-item label="Max Channels ">
                        <a-input v-model="form3.max_channels" placeholder="Default value is 1" />
                      </a-form-model-item>
                     </a-tooltip>
                     <a-tooltip placement="topLeft" title="Use ‘mean’ or ‘median’ to compute templates" arrow-point-at-center>
                      <a-form-model-item label="Mode">
                        <a-select v-model="form3.mode" placeholder="Default type is 'mean' ">
                          <a-select-option value="mean">
                            mean
                          </a-select-option>
                          <a-select-option value="Median">
                            Median
                          </a-select-option>
                        </a-select>
                      </a-form-model-item>
                    </a-tooltip>
                  </a-form-model>
                </a-collapse-panel>
                <a-collapse-panel key="5" header="Compute Unit PCA Scores">
                  <a-form-model :model="form4" :label-col="labelCol" :wrapper-col="wrapperCol">
                      <a-form-model-item label="Compute Unit PCA Scores">
                        <a-switch v-model="form4.compute_unit_pca_scores" />
                      </a-form-model-item>
                      <a-tooltip placement="topLeft" title="The sorting extractor" arrow-point-at-center>
                      <a-form-model-item label="Sorting">
                        <a-select v-model="form4.sorting" placeholder="Default type is 'fft' ">
                          <a-select-option value="fft">
                            fft
                          </a-select-option>
                          <a-select-option value="butter">
                            butter
                          </a-select-option>
                        </a-select>
                      </a-form-model-item>
                    </a-tooltip>
                     <a-tooltip placement="topLeft" title="List of unit ids to compute pca scores" arrow-point-at-center>
                      <a-form-model-item label="Unit Ids: ">
                        <a-input v-model="form4.unit_ids" placeholder="Input List, default is None" />
                      </a-form-model-item>
                     </a-tooltip>
                    <a-tooltip placement="topLeft" title="List of channels ids to compute pca from" arrow-point-at-center>
                      <a-form-model-item label="Channel Ids ">
                        <a-input v-model="form4.channel_ids" placeholder="Input List, default is None" />
                      </a-form-model-item>
                    </a-tooltip>
                    <a-tooltip placement="topLeft" title="List of indexes of used spikes for each unit" arrow-point-at-center>
                      <a-form-model-item label="Return Idxs ">
                        <a-switch v-model="form4.return_idxs" placeholder="Default is False"/>
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
    title: 'Get Unit Waveforms',
    content: 'Computes the spike waveforms from a recording and sorting extractor. The recording is split in chunks (the size in Mb is set with the chunk_mb argument) and all waveforms are extracted for each chunk and then re-assembled. If multiple jobs are used (n_jobs > 1), more and smaller chunks are created and processed in parallel'
  },
  {
    title: 'Get Unit Templates',
    content: 'Computes the spike templates from a recording and sorting extractor. If waveforms are not found as features, they are computed.'
  },
  {
    title: 'Get Unit Amplitudes',
    content: 'Computes the spike amplitudes from a recording and sorting extractor. Amplitudes can be computed in absolute value (uV) or relative to the template amplitude.'
  },
  {
    title: 'Get Unit Max Channels',
    content: 'Computes the spike maximum channels from a recording and sorting extractor. If templates are not found as property, they are computed'
  },
  {
    title: 'Compute Unit PCA Scores',
    content: 'Computes the PCA scores from the unit waveforms. If waveforms are not found as features, they are compute'
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
        get_unit_waveforms: false,
        sorting: '',
        unit_ids: '',
        channel_ids: '',
        return_idxs: false,
        chunk_size: '',
        chunk_mb: ''

      },
      form1: {
        get_unit_templates: false,
        sorting: '',
        unit_ids: '',
        channel_ids: '',
        mode: '',
        chunk_size: ''
      },
      form2: {
        get_unit_amplitudes: false,
        sorting: '',
        unit_ids: '',
        channel_ids: '',
        return_idxs: false
      },
      form3: {
        get_unit_max_channels: false,
        sorting: '',
        unit_ids: '',
        channel_ids: '',
        max_channels: '',
        mode: ''
      },
      form4: {
        compute_unit_pca_scores: false,
        sorting: '',
        unit_ids: '',
        channel_ids: '',
        return_idxs: false
      },
      ListData
    }
  },
  methods: {
    handleClick () {
      this.loading = !this.loading
    },
    onSubmit () {
      if (this.form.get_unit_waveforms === true) {
        if (this.form.sorting === '') {
          this.form.sorting = 'fft'
        }
        if (this.form.unit_ids === '') {
          this.form.unit_ids = 'None'
        }
        if (this.form.channel_ids === '') {
          this.form.channel_ids = 'None'
        }
        if (this.form.chunk_size === '') {
          this.form.chunk_size = 'None'
        }
        if (this.form.chunk_mb === '') {
          this.form.chunk_mb = 500
        }
        console.log('submit get_unit_waveforms', this.form)
      }
      if (this.form1.get_unit_templates === true) {
        if (this.form1.sorting === '') {
          this.form1.sorting = 'fft'
        }
        if (this.form1.unit_ids === '') {
          this.form1.unit_ids = 'None'
        }
        if (this.form1.channel_ids === '') {
          this.form1.channel_ids = 'None'
        }
        if (this.form1.mode === '') {
          this.form1.mode = 'mean'
        }
        if (this.form1.chunk_size === '') {
          this.form1.chunk_size = 'None'
        }
        console.log('submit get_unit_templates', this.form1)
      }
      if (this.form2.get_unit_amplitudes === true) {
        if (this.form2.sorting === '') {
          this.form2.sorting = 'fft'
        }
        if (this.form2.unit_ids === '') {
          this.form2.unit_ids = 'None'
        }
        if (this.form2.channel_ids === '') {
          this.form2.channel_ids = 'None'
        }
        console.log('submit get_unit_amplitudes', this.form2)
      }
      if (this.form3.get_unit_max_channels === true) {
        if (this.form3.sorting === '') {
          this.form3.sorting = 'fft'
        }
        if (this.form3.unit_ids === '') {
          this.form3.unit_ids = 'None'
        }
        if (this.form3.channel_ids === '') {
          this.form3.channel_ids = 'None'
        }
        if (this.form3.max_channels === '') {
          this.form3.max_channels = 1
        }
        if (this.form3.mode === '') {
          this.form3.mode = 'mean'
        }
        console.log('submit get_unit_max_channels', this.form3)
      }
      if (this.form4.compute_unit_pca_scores === true) {
        if (this.form4.sorting === '') {
          this.form4.sorting = 'fft'
        }
        if (this.form4.unit_ids === '') {
          this.form4.unit_ids = 'None'
        }
        if (this.form4.channel_ids === '') {
          this.form4.channel_ids = 'None'
        }
        console.log('submit compute_unit_pca_scores', this.form4)
      }
      this.current += 1
      this.$emit('changeCurrent', this.current)
    }
  }
}
</script>
