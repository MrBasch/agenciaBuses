<template>
  <v-dialog max-width="500px" v-model="edit">
    <v-card class="addDialog">
      <v-card-title class="cardTitle">Update or create station</v-card-title>
      <v-form>
        <v-text-field v-model="name" label="Enter station name"></v-text-field>
        <v-text-field v-model="code" label="Enter station code"></v-text-field>
        <v-text-field
          v-model="new_code"
          label="Enter station new_code"
        ></v-text-field>
        <v-select
          v-model="city_name"
          :items="cities_name"
          label="Select a city"
        ></v-select>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          @click.stop="updateStation(name, code, new_code, city_name)"
          color="#417D7A"
          >Update</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: "updateStationModal",
  props: ["edit"],
  data() {
    return {
      code: "",
      new_code: "",
      name: "",
      cities_name: [],
      cities: [],
      city_name: "",
    };
  },
  methods: {
    async updateStation(name, code, new_code, city_name) {
      const city = this.cities.filter((city) => city.name === city_name);
      await fetch(
        `http://127.0.0.1:8000/back/station?code=${code}&name=${name}&new_code=${new_code}&city_code=${city[0].code}`,
        {
          method: "PUT",
          mode: "cors",
          headers: {
            Authorization: `Token ${localStorage.token}`,
          },
          cache: "default",
        }
      ).then((res) => res.json().then((data) => console.log(data)));
    },
    async getCities() {
      await fetch("http://127.0.0.1:8000/back/city", {
        method: "GET",
        mode: "cors",
        headers: {
          Authorization: `Token ${localStorage.token}`,
        },
        cache: "default",
      }).then((res) =>
        res.json().then((data) => {
          data.map((city) => {
            this.cities.push(city);
            this.cities_name.push(city.name);
          });
        })
      );
    },
  },
  created() {
    this.getCities();
  },
};
</script>
<style scoped>
.addDialog {
  overflow: hidden;
  background-color: #8b8070;
}
.cardTitle {
  background-color: #1a3c40;
}
</style>