<script>
export default {
  methods: {
    onChange (a, b, c) {
      console.log(a, b, c)
    }
  }
}
</script>

<style scoped>
/* For demo */
.ant-carousel >>> .slick-slide {
  text-align: center;
  height: 470px;
  line-height: 160px;
  background: #364d79;
  overflow: hidden;
}

.ant-carousel >>> .slick-slide h3 {
  color: #fff;
}
</style>

<template>
  <div class="Search" >
    <div style="margin-top:30px;margin-left:30px;margin-right:30px">
      <a-carousel autoplay>
        <div><img src="@/assets/title1.jpg" style="width: 100%;height:100%"/></div>
        <div><img src="@/assets/title2.jpg" style="width: 100%;height:100%"/></div>
        <div><img src="@/assets/title3.jpg" style="width: 100%;height:100%"/></div>
        <div><img src="@/assets/title4.jpg" style="width: 100%;height:100%"/></div>
      </a-carousel>
    </div>

    <!-- <HelloWorld msg="TTDS Project Template"/> -->

    <!-- <br /><br /> -->
    <!-- <a-input-search placeholder="input search text" style="width: 200px" @search="onSearch" /> -->
    <!-- <br /><br /> -->
    <div>
        <h2 style='font-size:50px;margin-top:10px'>Are You Hungry?</h2>
    </div>
    <a-input-search style="margin-top:10px" size="large" placeholder="Search the food you want to cook" enter-button @search="onSearch" />
    <br /><br />
  <div>
    <br />
    <a-checkbox-group
    v-model="checkedList" :options="plainOptions" @change="onChange" />

  </div>

  </div>

</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import $backend from '../backend'
const plainOptions = [
  "Quick & Easy",
  "Calaries<500kcal",
  "Gluten Free",
  "Vegetarian",
];
const defaultCheckedList = [];

export default {
  name: "Search",
  components: {
    HelloWorld,
  },
  data() {
    return {
      checkedList: defaultCheckedList,
      indeterminate: true,
      checkAll: false,
      plainOptions,
    };
  },
  methods: {
    onChange(checkedList) {
      this.indeterminate =
        !!checkedList.length && checkedList.length < plainOptions.length;
      this.checkAll = checkedList.length === plainOptions.length;
    },
    onCheckAllChange(e) {
      Object.assign(this, {
        checkedList: e.target.checked ? plainOptions : [],
        indeterminate: false,
        checkAll: e.target.checked,
      })
      },

    onSearch (value) {
      top.location='https://ttds-project.herokuapp.com/#/search'
      localStorage.setItem('accessToken', value)
    },

  },
};
</script>

<style lang="scss">
</style>
