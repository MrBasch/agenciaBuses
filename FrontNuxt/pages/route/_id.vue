<template>
  <div class="main-detail" v-if="routes.length">
    <div class="header_" :key="routes">
      <h1>Route: {{ routes[0].name }}</h1>
    </div>
    <div class="detail">
      <p>Code = {{ routes[0].code }}</p>
      <p>Status = {{ routes[0].status }}</p>
      <p>Average selling places: = {{ average }}</p>
    </div>
    <div class="stops">
      <v-card color="#8b8070">
        <v-card-title class="cardTitle">Stations</v-card-title>
        <v-card-text class="card_buses">
          <ul>
            <li v-for="station in stops[0]" :key="station.code">
              <v-card color="white">
                <v-card-title class="cardTitle"
                  >Name = {{ station.name }}</v-card-title
                >
                <v-card-text>
                  <h2 style="color: #1a3c40">City {{ station.city.name }}</h2>
                  <h2 style="color: #1a3c40">Code:{{ station.code }}</h2>
                </v-card-text>
              </v-card>
            </li>
          </ul>
        </v-card-text>
      </v-card>
    </div>
    <v-card color="#8b8070">
      <v-card-title class="cardTitle">Buses</v-card-title>
      <v-form>
        <v-select
          v-model="number"
          :items="ten"
          label="N° selling places"
        ></v-select>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="#417D7A">filter</v-btn>
      </v-card-actions>
      <v-card-text class="card_buses">
        <ul>
          <li v-for="bus in buses[0]" :key="bus.code">
            <v-card color="white" v-if="bus.no_available_places >= number">
              <v-card-title class="cardTitle"
                >Bus:{{ bus.bus_code }}</v-card-title
              >
              <v-card-text>
                <h2 style="color: #1a3c40">Status= {{ bus.bus_status }}</h2>
                <h2 style="color: #1a3c40">
                  Seat sold= {{ bus.no_available_places }}
                </h2>
              </v-card-text>
            </v-card>
          </li>
        </ul>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: `Route ${this.id}`,
    };
  },
  data() {
    return {
      id: this.$route.params.id,
      routes: [],
      buses: [],
      stops: [],
      average: "",
      number: 0,
      ten: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    };
  },
  methods: {
    getPromPassenger() {
      const list_places = this.buses[0].map((bus) => bus.no_available_places);
      try {
        this.average =
          list_places.reduce((sum, curr) => sum + curr) / list_places.length;
      } catch (e) {
        this.average = 0;
      }
      console.log("wololo", this.average);
      // this.average = total / this.buses.length;
    },
    async getDetailRoute() {
      await fetch(
        `http://127.0.0.1:8000/back/detail_route?route_code=${this.id}`,
        {
          method: "GET",
          mode: "cors",
          headers: {
            Authorization: `Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`,
          },
          cache: "default",
        }
      ).then((res) =>
        res.json().then((data) => {
          console.log("data fetch=", data);
          this.routes.push(data.route);
          this.stops.push(data.route.stops);
          this.buses.push(data.selling_buses_places);
        })
      );
      this.getPromPassenger();
    },
  },
  created() {
    this.getDetailRoute();
  },
};
</script>
<style>
.main-detail {
  display: grid;
  gap: 2rem;
}
.cardTitle {
  margin-bottom: 2rem;
}
</style>