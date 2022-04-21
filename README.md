# pymetrics

  Metrics.start('golang_processing', 0)
  # do something
  Metrics.end('golang_processing', 0)
 
  @metrics('socket_connect', 0)
  def clientSocket():
    # do something

  print(Metrics.metrics_all)
  print(Metrics.metrics_all['socket_connect'])
  Metrics.clear()
