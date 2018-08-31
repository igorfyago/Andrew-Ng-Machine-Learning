function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%
eye_matrix = eye(num_labels);
y = eye_matrix(y, :);

a1 = [ones(m, 1) X];
z2 = a1 * Theta1';
a2 = [ones(size(z2, 1), 1) sigmoid(z2)];
z3 = a2 * Theta2';
a3 = sigmoid(z3);
h = a3
%Calculo el ultimo termino de la regularizacion, que basicamente suma todas las zhetas de las dos matrices
r = sum(sum(Theta1(:, 2 : end).^2)) + sum(sum(Theta2(:, 2 : end).^2));

%Calculo coste con regu
J =  -1/m * (sum(sum((y .* log(h) + (1 - y) .* log(1 - h))))) + lambda/(2 * m) * r;

%Calculo las deltas parciales
delta3 = h - y;
delta2 = delta3 * Theta2(:, 2 : end) .* sigmoidGradient(z2);

%Calculo las Theta_grads (lo que serian las deltas acumulativas)

Theta1_grad = delta2' * a1/m;
Theta2_grad = delta3' * a2/m;

%Añado la regularizacion a las Theta_grads, soy el puto amo:
r1 = (lambda/m) * [zeros(size(Theta1, 1), 1) Theta1(:, 2 : end)];
r2 = (lambda/m) * [zeros(size(Theta2, 1), 1) Theta2(:, 2 : end)];

Theta1_grad = Theta1_grad + r1;
Theta2_grad = Theta2_grad + r2;

%METODO CON FOR LOOP, ES MAS DIFICIL PERO ES LO QUE RECOMENDADO AL PRINCIPIO

%Añado columna de unos a la X

%X = [ones(m, 1) X ];

%Hago el loop y me quedan vectores verticales, hasta llegar al final con un 10 x 1:
%for i = 1 : m
 %   a1 = X(i, :)';
  %  z2 = Theta1 * a1;
   % a2 = [1; sigmoid(z2)];
    %z3 = Theta2 * a2;
    %a3 = sigmoid(z3);
   % h = a3;
%Ahora hago el vector de 10 x 1 para restarle a la hipotesis "h":
%yVec = (1:num_labels)' == y(i);

%Calculo la funcion coste "J":
%J = J + (-yVec' * log(h)) - (1 - yVec') * log(1 - h);

%Calculo el algoritmo backpropagation:
%delta3 = a3 - yVec;
%delta2 = Theta2' * delta3 .* a2 .*(1 - a2);

%Calculo las deltas mayusculas, que son las deltas minusculas acumuladas, pero se llaman Theta1_grad y Theta2_grad:
%Theta2_grad = Theta2_grad + delta3 * a2';
%Theta1_grad = Theta1_grad + delta2(2:end) * a1'; %La unidad bias de a2 no está conectada a a1

%Divido entre m la funcion coste "J" y el gradiente (derivadas, que las he calculado con el backprop):
%J = J/m;
%Theta2_grad = Theta2_grad/m;
%Theta1_grad = Theta1_grad/m;
    
  
    
    
    
    
    














% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
