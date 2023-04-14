// Add event listener to submit form for adding reports
const addReportForm = document.getElementById('add-report-form');
if (addReportForm) {
  addReportForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    fetch('/add_report', {
      method: 'POST',
      body: formData,
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log(data);
        // Clear form inputs
        addReportForm.reset();
      })
      .catch((error) => {
        console.error(error);
      });
  });
}

// Add event listener to submit form for adding data to database
const addDataForm = document.getElementById('add-data-form');
if (addDataForm) {
  addDataForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    fetch('/add_data', {
      method: 'POST',
      body: formData,
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log(data);
        // Clear form inputs
        addDataForm.reset();
      })
      .catch((error) => {
        console.error(error);
      });
  });
}

// Fetch data from cache if available, otherwise fetch from network
function fetchWithCache(url) {
  return caches.open('microbiology-reports-cache-v1').then((cache) => {
    return cache.match(url).then((response) => {
      const fetchPromise = fetch(url).then((networkResponse) => {
        cache.put(url, networkResponse.clone());
        return networkResponse;
      });
      return response || fetchPromise;
    });
  });
}

// Add event listener to load view reports page
const viewReportsTable = document.getElementById('view-reports-table');
if (viewReportsTable) {
  window.addEventListener('load', (e) => {
    e.preventDefault();
    fetchWithCache('/view_reports')
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.text();
      })
      .then((data) => {
        viewReportsTable.innerHTML = data;
      })
      .catch((error) => {
        console.error(error);
      });
  });
}
