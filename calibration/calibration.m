distance = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90,	95,	100, 105, 110, 115,	120, 125, 130, 135, 140];
voltages = [501.5, 439.75, 382.25, 343.75, 302.25, 261.75, 236.25, 213.75, 194.25, 180, 167.5, 159, 151, 136, 137, 124.25, 118.5, 110, 106.5, 103.25, 93.25, 90.5, 86, 84.25, 81.25];

T = table(distance, voltages);

hold on;
plot(distance, voltages, 'b*');

%[volts, ~, mu] = polyfit(T.distance, T.avg_voltage, 5);
%f = polyval(volts, distance, [], mu);
%plot(distance, f, 'r');
distance = distance.';
voltages = voltages.';

f = fit(distance, voltages, 'exp1')
plot(f, distance, voltages, 'r');
hold off;

