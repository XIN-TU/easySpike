<template>
  <a-layout id="components-layout-demo-fixed">
    <a-layout-header :style="{ zIndex: 1, width: '100%',height:'200px', lineHeight:'10px', background:'#183D4E',paddingBottom:'0px'}">
      <h1 class="logo"> Easy Spike Sorting </h1>
      <h5 class="logo"> based by SpikeInterface </h5>
    </a-layout-header>
    <a-layout-content>
      <!-- <div :style="{position:fixed,marginTop:'0px', background: '#f0f0f0', minHeight: '1000px'}">
        <router-view/>
      </div> -->
      <router-view/>
    </a-layout-content>
    <a-layout-footer :style="{ textAlign: 'center' }">
      Ant Design ©2018 Created by Ant UED
    </a-layout-footer>
  </a-layout>
</template>

<script>
export default {
  data () {
    return {
    }
  }
}
</script>
<style lang="scss">
#components-layout-demo-fixed .logo {
  padding-top: 45px;
  color: #bfbfbf;
  text-align: center;
  font-size: 300%;
  font-weight:200;
  font-style:normal;
}

</style>
