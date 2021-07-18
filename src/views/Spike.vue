<template>
<div>
      <a-steps v-model="current" type="navigation" size="large" :style="stepStyle" class="header-steps" @change="onChange">
        <a-step
          title="Step 1"
          sub-title="Loding Recording"
          :status="status0"
          description="This is a description."
        />
        <a-step
          title="Step 2"
          sub-title="Pre-processing"
          :status="status1"
          description="This is a description."
        />
        <a-step
          title="Step 3"
          sub-title="Spike Sorting"
          :status="status2"
          description="This is a description."
        />
        <a-step
          title="Step 4"
          sub-title="Post-processing"
          :status="status3"
          description="This is a description."
        />
        <a-step
          title="Step 5"
          sub-title="Validation"
          :status="status4"
          description="This is a description."
        />
        <a-step
          title="Step 6"
          sub-title="Results"
          :status="status5"
          description="This is a description."
        />
      </a-steps>

  <component v-bind:is="compo" :current = 'current' @changeCurrent="changeCurrent" class='flow'></component>
</div>
</template>

<script>
import Flow1 from '@/components/Flow1.vue'
import Flow2 from '@/components/Flow2.vue'
import Flow3 from '@/components/Flow3.vue'
import Flow4 from '@/components/Flow4.vue'
import Flow5 from '@/components/Flow5.vue'
import Flow6 from '@/components/Flow6.vue'
export default {
  name: 'Spike',
  components: {
    Flow1,
    Flow2,
    Flow3,
    Flow4,
    Flow5,
    Flow6
  },
  data () {
    return {
      current: 0,
      stepStyle: {
        marginBottom: '0px',
        boxShadow: '0px -1px 0 0 #e8e8e8 inset'
      },
      status0: 'process',
      status1: 'wait',
      status2: 'wait',
      status3: 'wait',
      status4: 'wait',
      status5: 'wait',
      compo: Flow1
    }
  },
  methods: {
    changeCurrent (val) {
      this.onChange(val)
      this.current = val
      console.log(this.status0, this.status1, this.status2)
    },
    onChange (current) {
      switch (current) {
        case 0:
          this.status0 = 'process'
          this.status1 = 'wait'
          this.status2 = 'wait'
          this.status3 = 'wait'
          this.status4 = 'wait'
          this.status5 = 'wait'
          this.compo = Flow1
          break
        case 1:
          this.status0 = 'finish'
          this.status1 = 'process'
          this.status2 = 'wait'
          this.status3 = 'wait'
          this.status4 = 'wait'
          this.status5 = 'wait'
          this.compo = Flow2
          break
        case 2:
          this.status0 = 'finish'
          this.status1 = 'finish'
          this.status2 = 'process'
          this.status3 = 'wait'
          this.status4 = 'wait'
          this.status5 = 'wait'
          this.compo = Flow3
          break
        case 3:
          this.status0 = 'finish'
          this.status1 = 'finish'
          this.status2 = 'finish'
          this.status3 = 'process'
          this.status4 = 'wait'
          this.status5 = 'wait'
          this.compo = Flow4
          break
        case 4:
          this.status0 = 'finish'
          this.status1 = 'finish'
          this.status2 = 'finish'
          this.status3 = 'finish'
          this.status4 = 'process'
          this.status5 = 'wait'
          this.compo = Flow5
          break
        case 5:
          this.status0 = 'finish'
          this.status1 = 'finish'
          this.status2 = 'finish'
          this.status3 = 'finish'
          this.status4 = 'finish'
          this.status5 = 'process'
          this.compo = Flow6
          break
      }
    }
  }
}
</script>

<style lang="scss">
.flow{
  padding-left: 10%;
  padding-right: 10%;
}
.header-steps{
  border-bottom: 0px solid #ddd;
  padding-top: 15px;
  box-shadow: 0 1px 4px #ffffff;
  background: white;
  margin-top: 0px;
}
</style>
