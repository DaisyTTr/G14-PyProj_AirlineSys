---


---

<h1 id="report">REPORT</h1>
<blockquote>
<p>Group 14: Airline Booking Information Management System</p>
<p>Members:<br>
Nguyễn Thanh Trang Bi9-219<br>
Đặng Hùng Kiên Bi9-133<br>
Lê Phước Long Bi9-153<br>
Lê Duy Anh Bi9-034</p>
</blockquote>
<h2 id="what-this-program-does">What this program does</h2>
<blockquote>
<ul>
<li>Airline Booking Information Management System contains the detail about flight schedules, passenger information like their name, date of birth, their reservations and ticket records.</li>
<li>We plan to build a system to store the passenger information (like their name sort by id, their date of birth to reduce the duplication problem, their chosen class, seat, place from where to where…), flight information (like flight name, update flight information, view flight), to manage</li>
</ul>
</blockquote>
<h2 id="why-to-use">Why to use</h2>
<ul>
<li>For admin:</li>
</ul>
<blockquote>
<ul>
<li>Helps travel companies to integrate all flight-related data into online portal to provide customer with wide variety of flight options with competitive flight fares.</li>
<li>Update flight imediately by adding new, delete, cancel flight.</li>
</ul>
</blockquote>
<ul>
<li>For passenger:</li>
</ul>
<blockquote>
<ul>
<li>Have a clear information about update cancel flight.</li>
<li>Help passenger to view all the schedule of flight.</li>
<li>Book a flight faster and easier</li>
</ul>
</blockquote>
<h2 id="how-we-create">How we create</h2>
<h3 id="database-schema">Database schema</h3>
<p><img src="https://github.com/DaisyTTr/G14-PyProj_AirlineSys/blob/main/Database%20diagram.png" alt="Database diagram"></p>
<h3 id="python-module">Python module</h3>
<blockquote>
<ul>
<li>Registration module: ask passenger their information, passenger can login their account and view all flight detail</li>
<li>Administration module: admin can manage the site, update, delete, view passenger list, cancel ticket, update flight schedule</li>
<li>Passenger module: user can login their account to view schedule, book ticket, cancel ticket.</li>
</ul>
</blockquote>
<ul>
<li>tkinter: to made UI</li>
</ul>
<h3 id="classes">Classes</h3>
<blockquote>
<ul>
<li>Airlines booking class: manage all the operation of Airlines booking.</li>
</ul>
</blockquote>
<blockquote>
<ul>
<li>Staff class: manage all the operation of staff.</li>
</ul>
</blockquote>
<blockquote>
<ul>
<li>Ticket booking class: manage all the operation of Ticket booking.</li>
</ul>
</blockquote>
<h3 id="inputoutput">Input/Output</h3>
<ul>
<li>Input:</li>
</ul>
<blockquote>
<ul>
<li>Name</li>
<li>Date of birth</li>
<li>From</li>
<li>To</li>
<li>Seat Class</li>
<li>Seat</li>
<li>Plane ID</li>
</ul>
</blockquote>
<ul>
<li>Output</li>
</ul>
<h2 id="ui-structure">UI structure</h2>

