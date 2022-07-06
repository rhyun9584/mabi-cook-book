const bookChart = document.getElementById("bookChart").getContext('2d');

const chart = new Chart(bookChart, {
    type: 'pie',
    data: {
        labels: ['미수집', '수집', '5성 수집'],
        datasets: [
            {
                label: '',
                data: [state0, state1, state2],
                backgroundColor: [
                    'lightgrey',
                    'lightgreen',
                    'rgb(255, 242, 0)',
                ],
            },
        ],
    },
    options: {
        responsive: false,
    },
});