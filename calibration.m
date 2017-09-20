distance = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90,	95,	100, 105, 110, 115,	120, 125, 130, 135, 140];
voltages = [501.5, 439.75, 382.25, 343.75, 302.25, 261.75, 236.25, 213.75, 194.25, 180, 167.5, 159, 151, 136, 137, 124.25, 118.5, 110, 106.5, 103.25, 93.25, 90.5, 86, 84.25, 81.25];

new_distances = [24, 37, 43, 53, 61, 71, 83, 97, 108, 121];
new_voltages = [456, 316, 272, 225, 197.5, 169.75, 140, 113, 98, 91];

v = SensorVal1;
p = ServoPos1;

syms a;
sad=[];
for v=1:length(SensorVal1)
    s = vpasolve(744.4.*exp(-.04263*a) + 216.*exp(-.0071584*a) == SensorVal1(v), a);
    sad = [sad; s];
end


% hold on;
% plot(distance, voltages, 'b*');
% 
% x = linspace(0,200, 400);
% y1 = 657.7.*exp(-.01818.*x);
% y2 = 744.4.*exp(-.04263*x) + 216.*exp(-.0071584*x);
% %plot(x,y1,'r');
% plot(x, y2, 'r');
% 
% plot(new_distances, new_voltages, 'ok', 'LineWidth', 3);
% 
% xlabel('Distance from sensor');
% ylabel('Sensor Reading');
% 
% legend('calibration points', 'calibration line', 'test points');
% axis([20 140 75 525])
% hold off;

plot(ServoPos1, sad);

